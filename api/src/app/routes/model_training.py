from fastapi import APIRouter, status

from src.app.services.model_service import get_current_room_with_model, get_last_data
from src.models import Message
from collections import Counter

router = APIRouter()

@router.get("/get-esp-position", status_code=status.HTTP_200_OK)
def get_esp_position(esp_id):
    flag = True
    num_try = 0
    room = ""
    while num_try < 3:
        dfs = get_last_data(esp_id) 

        list_result = []
        for date, df in dfs.items(): 
            result = get_current_room_with_model(df)
            list_result.append(result)

        room_counts = Counter(list_result)
        
        # print(list_result)
        # print(room_counts.most_common(2))
        
        room_most_common = room_counts.most_common(2)
        
        if len(room_most_common) > 1:
            if room_most_common[0][1] == room_most_common[1][1]:
                num_try += 1
                print("num_try: ", num_try)
            elif room_most_common[0][1] > room_most_common[1][1]:
                room = room_most_common[0][0]
                num_try = 5
        else:
            num_try += 1

    print(f"return room: {room} - num_try: {num_try}")
    return room



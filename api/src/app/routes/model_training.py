from fastapi import APIRouter, status

from src.app.services.model_service import get_current_room_with_model, get_last_data
from src.models import Message

router = APIRouter()

@router.get("/get-esp-position", status_code=status.HTTP_200_OK) # esse endpoint deveria ser assíncrono?
def get_esp_position(esp_id):
    df = get_last_data(esp_id) # poderia ter uma validação um pouco mais assertiva? 

    result = get_current_room_with_model(df)

    return result



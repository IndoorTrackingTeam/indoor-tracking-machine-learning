# from autogluon.tabular import TabularDataset, TabularPredictor
from datetime import datetime, timedelta
import requests
import pandas as pd
import os

# from dotenv import load_dotenv

# load_dotenv()

def get_last_data(esp_id):
    url = f'https://run-api-dev-131050301176.us-east1.run.app/router/data/get-last-data-from-esp-id?esp_id={esp_id}'
    response = requests.get(url)

    data = response.json()

    first_key = next(iter(data))  # Obter a primeira chave
    print("Primeira chave:", first_key)
    data_aux = datetime.strptime(first_key, "%Y-%m-%d %H:%M:%S")
    max_interval = timedelta(minutes=2)

    dfs = {}
    for date, item in data.items():
        print("Data recebida:", date)

        if data_aux - (datetime.strptime(date, "%Y-%m-%d %H:%M:%S")) < max_interval:
            print("dentro do time: ", item)
            df = pd.DataFrame.from_dict(item)
            
            dfs[date] = df
        else:
            print("para a lista")
            break

    print(dfs)

    return dfs

def get_current_room_with_model(data):
    MODEL = os.getenv('MODEL')
    MODEL_PATH = os.getenv('MODEL_PATH')
    
    predictor = TabularPredictor.load(MODEL_PATH)
    
    predictions = predictor.predict(data, model=MODEL)

    return predictions[0]
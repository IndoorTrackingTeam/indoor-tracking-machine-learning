from autogluon.tabular import TabularDataset, TabularPredictor
import requests
import pandas as pd
import os

def get_last_data(esp_id):
    url = f'https://run-api-dev-131050301176.us-east1.run.app/router/data/get-last-data-from-esp-id?esp_id={esp_id}'
    response = requests.get(url)

    data = response.json()

    print(data[0])

    df = pd.DataFrame.from_dict(data)

    return df

def get_current_room_with_model(data):
    MODEL = os.getenv('MODEL')
    MODEL_PATH = os.getenv('MODEL_PATH')
    
    print(MODEL)
    print(MODEL_PATH)
    print(os.listdir())
    
    predictor = TabularPredictor.load(MODEL_PATH)
    
    predictions = predictor.predict(data, model=MODEL)

    return predictions[0]
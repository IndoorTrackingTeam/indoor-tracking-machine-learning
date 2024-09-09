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
    MODEL_PATH = os.getenv('PATH')
    MODEL = os.getenv('MODEL')
    
    # Carregar o preditor salvo
    predictor = TabularPredictor.load(MODEL_PATH)
    
    # Fazer predições nos novos dados usando o modelo escolhido
    predictions = predictor.predict(data, model=MODEL)

    # Exibir as predições
    # print(f"resultado final: {predictions[0]}")
    return predictions[0]
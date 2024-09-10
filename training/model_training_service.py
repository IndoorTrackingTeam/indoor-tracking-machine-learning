import os
import requests
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

def get_data_for_training():
    url = 'https://run-api-dev-131050301176.us-east1.run.app/router/training-data/get-data-for-training'
    response = requests.get(url)

    data = response.json()

    df1 = pd.DataFrame.from_dict(data[0])
    df2 = pd.DataFrame.from_dict(data[1])

    return df1, df2

def create_predictor(train_data, test_data):
    predictor = TabularPredictor(label='room').fit(train_data)

    y_pred = predictor.predict(test_data.drop(columns=['room']))
    y_pred.head()

    predictor.evaluate(test_data, silent=True)

    best_model = predictor.get_model_best()

    model_path = predictor.path

    return best_model, model_path

train_df, test_df = get_data_for_training()
best_model, model_path = create_predictor(train_df, test_df)


with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
    env_file.write(f"MODEL={best_model}\n")
    env_file.write(f"MODEL_PATH={model_path}\n")
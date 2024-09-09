import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
import requests

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

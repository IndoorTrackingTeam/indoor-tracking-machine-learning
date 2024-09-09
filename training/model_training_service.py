import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
import requests

def get_data_for_training():
    url = 'https://run-api-dev-131050301176.us-east1.run.app/router/training-data/get-data-for-training'
    response = requests.get(url)
    # print(response.json())

    data = response.json()

    df1 = pd.DataFrame.from_dict(data[0])
    df2 = pd.DataFrame.from_dict(data[1])

    df1.to_csv("data/dataframe_training.csv", index=False)
    df2.to_csv("data/dataframe_test.csv", index=False)

    return df1, df2


def create_predictor(train_data, test_data):

    #Exibir as primeiras linhas do dataset
    print(train_data.head())

    #Escolher coluna de saída
    label = 'room'

    #Observar coluna de saída
    print(train_data[label].describe())

    #Treinar modelos
    predictor = TabularPredictor(label=label).fit(train_data)

    y_pred = predictor.predict(test_data.drop(columns=[label]))
    y_pred.head()

    predictor.evaluate(test_data, silent=True)

    predictor.leaderboard(test_data)

# def train_model():
train_df, test_df = get_data_for_training()
create_predictor(train_df, test_df)
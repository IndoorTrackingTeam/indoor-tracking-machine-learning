import os
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from typing import Generator
from main import api
import pytest
from src.app.routes.model_training import get_esp_position

# from collections import Counter
# from src.app.services.model_service import get_last_data
    
# Fixture para instanciar um cliente
@pytest.fixture(scope="function", autouse=True)
def client() -> Generator:
    with TestClient(api) as client:
        yield client

# Testando se a requisição está sendo feita corretamente
@patch('src.app.services.model_service.requests.get')
@patch('src.app.routes.model_training.get_current_room_with_model')
def test_get_esp_position_success(mock_get_current_room_with_model, mock_get, client: TestClient):

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "2022-11-05 20:23:32": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -83,
            "C8:CC:E5:5D:AE:FD": -62,
            "FC:22:F4:ED:1A:16": -86
        }],
        "2022-11-05 20:22:43": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -88,
            "C8:CC:E5:5D:AE:FD": -66,
            "FC:22:F4:ED:1A:16": -92
        }]
    }
    mock_get.return_value = mock_response

    mock_get_current_room_with_model.return_value = "room_1"
    response = client.get("/model-training/get-esp-position?esp_id=12345")

    assert response.status_code == 200
    assert response.json() == "room_1"

# Testando se a requisição está sendo feita corretamente no caso de um empate
@patch('src.app.services.model_service.requests.get')
@patch('src.app.routes.model_training.get_current_room_with_model')
def test_get_esp_position_success_when_ties(mock_get_current_room_with_model, mock_get, client: TestClient):

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "2022-11-05 20:24:05": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -80,
            "C8:CC:E5:5D:AE:FD": -66,
            "FC:22:F4:ED:1A:16": -92
        }],
        "2022-11-05 20:23:50": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -70,
            "C8:CC:E5:5D:AE:FD": -60,
            "FC:22:F4:ED:1A:16": -90
        }],
        "2022-11-05 20:23:32": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -83,
            "C8:CC:E5:5D:AE:FD": -62,
            "FC:22:F4:ED:1A:16": -86
        }],
        "2022-11-05 20:22:43": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -88,
            "C8:CC:E5:5D:AE:FD": -66,
            "FC:22:F4:ED:1A:16": -92
        }]
    }
    mock_get.return_value = mock_response

    # Caso de empate ele tenta verificar 3 vezes no máximo, com os 5 ultimos dados do esp
    # Nesse caso teremos 4 dados do esp que serão repetidos para os 3 testes,
    # assim como eu tenho que empatar as tres vezes minha resposta na tentativa deverá ser essa
    # "room_1", "room_1", "room_2", "room_2"
    # então para cada tentativa teremos a mesma resposta.
    mock_get_current_room_with_model.side_effect = ["room_1", "room_1", "room_2", "room_2", "room_1", "room_1", "room_2", "room_2", "room_1", "room_1", "room_2", "room_2"]
    response = client.get("/model-training/get-esp-position?esp_id=12345")

    assert response.status_code == 200
    assert response.json() == ""


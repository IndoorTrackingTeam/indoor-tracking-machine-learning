from unittest.mock import MagicMock, patch
from src.app.services.model_service import get_last_data
import pandas as pd

# Teste para verificar um fluxo de sucesso para a função
@patch('src.app.services.model_service.requests.get')
def test_get_last_data_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "2022-11-05 20:24:20": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -71,
            "C8:CC:E5:5D:AE:FD": -65,
            "FC:22:F4:ED:1A:16": -87
        }],
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

    esp_id = "12345"
    result = get_last_data(esp_id)

    assert "2022-11-05 20:23:32" in result
    assert isinstance(result["2022-11-05 20:23:32"], pd.DataFrame)
    assert result["2022-11-05 20:23:32"]["38:11:DF:A5:A2:FA"].values == -83

# Teste para o limite do intervalo de tempo
@patch('src.app.services.model_service.requests.get')
def test_get_last_data_time_interval(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
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
        "2022-11-05 20:20:43": [{
            "FC:22:F4:EF:16:00": 0,
            "38:11:DF:A5:A2:FA": -88,
            "C8:CC:E5:5D:AE:FD": -66,
            "FC:22:F4:ED:1A:16": -92
        }]
    }
    mock_get.return_value = mock_response

    esp_id = "12345"
    result = get_last_data(esp_id)

    assert "2022-11-05 20:20:43" not in result
    assert "2022-11-05 20:23:50" in result
    assert "2022-11-05 20:23:32" in result

    
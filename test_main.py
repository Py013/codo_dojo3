from main import get_temperature_api

from unittest import mock
from unittest.mock import MagicMock
import requests

import pytest

@pytest.fixture(autouse=True)
def json_resposta():
    return {
        "current_condition":
        [
            {"temp_C": 22} 
        ]
    }

@mock.patch("requests.get")
def test_get_temperature_api(mock_requests):
    """Deve testar a chamada para a API"""
    # O 'assert' é a chave! Ele verifica se a condição é verdadeira.
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "current_condition":
        [
            {"temp_C": 22} 
        ]
    }
    mock_requests.return_value = mock_response
    assert get_temperature_api("Santos") == 22


def test_get_cols():
    col_names = csv_col_names()
    assert col_names[2] == "temperatura_c" 

def test_get_number_cols():
    col_num = get_number_cols()
    assert col_num == 3

def test_all_cols_have_temp():
    cities = read_cities_with_temp()
    assert len(cities[2]) == len(cities[1])

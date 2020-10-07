import requests_mock
from src.processor import Processor
from tests.fixtures import INSTANCES


def test_lista_instancias():
    p = Processor()
    expected = {'instancias': INSTANCES}
    with requests_mock.Mocker() as mock_request:
        mock_request.get('http://localhost:3000/dev/instances', json=expected)
        response = p.lista_instancias()
    assert response == expected

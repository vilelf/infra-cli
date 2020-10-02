import requests_mock

from processor import Processor


def test_lista_instancias():
    p = Processor()
    expected = {'instancias': []}
    with requests_mock.Mocker() as mock_request:
        mock_request.get(p.BASE_URL, json=expected)
        response = p.lista_instancias()
    assert response == expected

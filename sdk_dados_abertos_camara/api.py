import requests

from sdk_dados_abertos_camara.exceptions import CamaraAPIException

BASE_URL = 'https://dadosabertos.camara.leg.br/api/v2/'
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


def get_one(endpoint, data_only=True):
    """
    Get a single entity from an endpoint, e.g. /deputados/{id}
    """
    res = requests.get(BASE_URL + endpoint, headers=HEADERS)
    if res.status_code > 299:
        raise CamaraAPIException(res.status_code, endpoint)

    return res.json().get('dados', {}) if data_only else res.json()


def get(endpoint,
        extra_params={},
        order=None,
        orderBy=None,
        page=1,
        itens=20,
        data_only=True):
    """
    Get a list of entities from an endpoint, e.g. /deputados
    """
    params = {'pagina': page, 'itens': itens}
    if order:
        params.update({'ordem': order})
    if orderBy:
        params.update({'ordenarPor': orderBy})

    params.update(extra_params)

    res = requests.get(BASE_URL + endpoint, headers=HEADERS, params=params)
    if res.status_code > 299:
        raise CamaraAPIException(res.status_code, endpoint)

    return res.json().get('dados', []) if data_only else res.json()

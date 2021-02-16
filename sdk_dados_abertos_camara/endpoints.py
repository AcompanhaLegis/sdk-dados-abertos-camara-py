from sdk_dados_abertos_camara import api, exceptions
from sdk_dados_abertos_camara.models import Bloco


DEFAULT_PARAMS = {
    'page': 1,
    'itens': 20,
    'data_only': True
}


def get_blocos(id=None, id_legislatura=None, params=DEFAULT_PARAMS):
    extra_params = {}
    if id:
        extra_params['id'] = id

    if id_legislatura:
        extra_params['id_legislatura'] = id_legislatura

    res = api.get('/blocos', extra_params=extra_params, **params)
    if params['data_only']:
        return [Bloco(b) for b in res]

    return res


def get_bloco(id, data_only=True):
    if not id or not isinstance(id, int):
        raise exceptions.CamaraAPIInvalidID('/blocos/{id}')

    res = api.get_one('/blocos/{}'.format(id), data_only)

    if data_only:
        return Bloco(res)

    return res

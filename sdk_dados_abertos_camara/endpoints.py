from sdk_dados_abertos_camara import api, exceptions
from sdk_dados_abertos_camara.models import Bloco, Deputado, DespesaDeputado
from sdk_dados_abertos_camara.utils import to_camelcase


DEFAULT_PARAMS = {
    'page': 1,
    'itens': 20,
    'data_only': True
}


def _get_extra_args(all_args, exclude=[]):
    extra_params = {}
    for key in all_args:
        if key != 'params' and all_args[key] and key not in exclude:
            extra_params[to_camelcase(key)] = all_args[key]
    return extra_params


def _get_params(params):
    updated_params = DEFAULT_PARAMS
    updated_params.update(params)
    return updated_params


def get_blocos(id=None, id_legislatura=None, params={}):
    extra_params = _get_extra_args(locals())
    params = _get_params(params)

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


def get_deputados(id=None,
                  nome=None,
                  id_legislatura=None,
                  sigla_uf=None,
                  sigla_partido=None,
                  sigla_sexo=None,
                  data_inicio=None,
                  data_fim=None,
                  params={}):
    extra_params = _get_extra_args(locals())
    params = _get_params(params)

    res = api.get('/deputados', extra_params, **params)
    if params['data_only']:
        return [Deputado(d) for d in res]

    return res


def get_deputado(id=None, data_only=True):
    extra_params = _get_extra_args(locals())

    res = api.get_one('/deputados/{}'.format(id), data_only)
    if data_only:
        return Deputado(res)

    return res


def get_deputado_despesas(id,
                          id_legislatura=None,
                          ano=None,
                          mes=None,
                          cnpj_cpf_fornecedor=None,
                          params={}):

    extra_params = _get_extra_args(locals(), ['id'])
    params = _get_params(params)
    res = api.get('/deputados/{}/despesas'.format(id), extra_params, **params)

    if params['data_only']:
        return [DespesaDeputado(d) for d in res]

    return res

from datetime import datetime


DATETIME_FORMAT = '%Y-%m-%dT%H:%M'
DATE_FORMAT = '%Y-%m-%d'


class Model(object):
    """
    Default model.
    """

    def __init__(self, data):
        self.data = data

    def get_date(self, date_str, fmt=DATETIME_FORMAT):
        """
        Since the data comes from the API, we shouldn't validate it,
        so if there's no data (TypeError when None) or it is empty (ValueError)
        it returns an empty string.
        """
        try:
            date = datetime.strptime(date_str, fmt)
        except (TypeError, ValueError):
            return ''
        else:
            return date

    def __dict__(self):
        return self.data


class Bloco(Model):
    """
    {
        "id": "string",
        "idLegislatura": "string",
        "nome": "string",
        "uri": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.id = data['id']
        self.id_legislatura = data['idLegislatura']
        self.uri = data['uri']
        self.nome = data['nome']

    def __str__(self):
        return self.nome


class Deputado(Model):
    """
    {
        "email": "string",
        "id": 0,
        "idLegislatura": 0,
        "nome": "string",
        "siglaPartido": "string",
        "siglaUf": "string",
        "uri": "string",
        "uriPartido": "string",
        "urlFoto": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.id = data['id']
        self.id_legislatura = data['idLegislatura']
        self.nome = data['nome']
        self.sigla_partido = data['siglaPartido']
        self.sigla_uf = data['siglaUf']
        self.uri = data['uri']
        self.uri_partido = data['uriPartido']
        self.url_foto = data['urlFoto']

    def __str__(self):
        return self.nome


class LocalCamara(Model):
    """
    This model represents a location inside the Camara dos Deputados building,
    but it isn't an entity in their API, it is present as part of an Evento.
    {
        "andar": "string",
        "nome": "string",
        "predio": "string",
        "sala": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        if data:
            self.andar = data.get('andar', '')
            self.nome = data.get('nome', '')
            self.predio = data.get('predio', '')
            self.sala = data.get('sala', '')

    def __str__(self):
        if not self.data:
            return ''
        return self.nome


class Orgao(Model):
    """
    {
        "apelido": "string",
        "codTipoOrgao": 0,
        "id": 0,
        "nome": "string",
        "nomePublicacao": "string",
        "sigla": "string",
        "tipoOrgao": "string",
        "uri": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.apelido = self.data['apelido']
        self.cod_tipo_orgao = self.data['codTipoOrgao']
        self.id = self.data['id']
        self.nome = self.data['nome']
        self.nome_publicacao = self.data['nomePublicacao']
        self.sigla = self.data['sigla']
        self.tipo_orgao = self.data['tipoOrgao']
        self.uri = self.data['uri']

    def __str__(self):
        return self.nome


class Evento(Model):
    """
    {
        "dataHoraFim": "string",
        "dataHoraInicio": "string",
        "descricao": "string",
        "descricaoTipo": "string",
        "id": 0,
        "localCamara": {
          "andar": "string",
          "nome": "string",
          "predio": "string",
          "sala": "string"
        },
        "localExterno": "string",
        "orgaos": [
          {
            "apelido": "string",
            "codTipoOrgao": 0,
            "id": 0,
            "nome": "string",
            "nomePublicacao": "string",
            "sigla": "string",
            "tipoOrgao": "string",
            "uri": "string"
          }
        ],
        "situacao": "string",
        "uri": "string",
        "urlRegistro": "string"
    }
    """

    def __init__(self, data):
        self.data = data
        self.data_hora_fim = self.get_date(self.data['dataHoraFim'])
        self.data_hora_inicio = self.get_date(self.data['dataHoraInicio'])
        self.descricao = self.data['descricao']
        self.descricao_tipo = self.data['descricaoTipo']
        self.id = self.data['id']
        self.local_camara = LocalCamara(self.data['localCamara'])
        self.local_externo = self.data['localExterno']
        self.orgaos = [Orgao(o) for o in self.data['orgaos']]
        self.situacao = self.data['situacao']
        self.uri = self.data['uri']
        self.url_registro = self.data['urlRegistro']

    def __str__(self):
        return self.nome


class Frente(Model):
    """
    {
        "id": 0,
        "idLegislatura": 0,
        "titulo": "string",
        "uri": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.id = self.data['id']
        self.id_legislatura = self.data['idLegislatura']
        self.titulo = self.data['titulo']
        self.uri = self.data['uri']

    def __str__(self):
        return self.titulo


class Legislatura(Model):
    """
    {
        "dataFim": "string",
        "dataInicio": "string",
        "id": 0,
        "uri": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.data_fim = self.get_date(
            self.data.get('dataFim', None), DATE_FORMAT)
        self.data_inicio = self.get_date(
            self.data.get('dataInicio', None), DATE_FORMAT)
        self.id = self.data['id']
        self.uri = self.data['uri']

    def __str__(self):
        return 'Legislatura ID: {}'.format(self.id)


class Partido(Model):
    """
    {
      "id": "string",
      "nome": "string",
      "sigla": "string",
      "uri": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.id = self.data['id']
        self.nome = self.data['nome']
        self.sigla = self.data['sigla']
        self.uri = self.data['uri']

    def __str__(self):
        return self.sigla


class StatusProposicao(Model):
    """
    This model represents a Status from a Proposicao.
    It's also not an entity from the API.
    {
        "dataHora": "string",
        "sequencia": 0,
        "siglaOrgao": "string",
        "uriOrgao": "string",
        "uriUltimoRelator": "string",
        "regime": "string",
        "descricaoTramitacao": "string",
        "codTipoTramitacao": "string",
        "descricaoSituacao": "string",
        "codSituacao": 0,
        "despacho": "string",
        "url": "string",
        "ambito": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.data_hora = self.get_date(self.data['dataHora'], DATE_FORMAT)
        self.sequencia = self.data['sequencia']
        self.sigla_orgao = self.data['siglaOrgao']
        self.uri_orgao = self.data['uriOrgao']
        self.regime = self.data['regime']
        self.descricao_tramitacao = self.data['descricaoTramitacao']
        self.cod_tipo_tramitacao = self.data['codTipoTramitacao']
        self.cod_situacao = self.data['codSituacao']
        self.despacho = self.data['despacho']
        self.url = self.data['url']
        self.ambito = self.data['ambito']

    def __str__(self):
        return self.nome

    def __lt__(self, other):
        return self.sequencia < other.sequencia


class Proposicao(Model):
    """
    {
        "id": 0,
        "uri": "string",
        "siglaTipo": "string",
        "codTipo": 0,
        "numero": 0,
        "ano": 0,
        "ementa": "string",
        "dataApresentacao": "string",
        "uriOrgaoNumerador": "string",
        "statusProposicao": {
            "dataHora": "string",
            "sequencia": 0,
            "siglaOrgao": "string",
            "uriOrgao": "string",
            "uriUltimoRelator": "string",
            "regime": "string",
            "descricaoTramitacao": "string",
            "codTipoTramitacao": "string",
            "descricaoSituacao": "string",
            "codSituacao": 0,
            "despacho": "string",
            "url": "string",
            "ambito": "string"
        },
        "uriAutores": "string",
        "descricaoTipo": "string",
        "ementaDetalhada": "string",
        "keywords": "string",
        "uriPropPrincipal": "string",
        "uriPropAnterior": "string",
        "uriPropPosterior": "string",
        "urlInteiroTeor": "string",
        "urnFinal": "string",
        "texto": "string",
        "justificativa": "string"
    }
    If not from the endpoint /proposicao/{id} this entity has only:
    {
        "id": 0,
        "uri": "string",
        "siglaTipo": "string",
        "codTipo": 0,
        "numero": 0,
        "ano": 0,
        "ementa": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.id = self.data['id']
        self.uri = self.data['uri']
        self.sigla_tipo = self.data['siglaTipo']
        self.cod_tipo = self.data['codTipo']
        self.numero = self.data['numero']
        self.ano = self.data['ano']
        self.ementa = self.data['ementa']
        self.data_apresentacao = self.get_date(
            self.data.get('dataApresentacao'))
        self.uri_orgao_numerador = self.data.get('uriOrgaoNumerador', None)
        self.status_proposicao = StatusProposicao(
            self.data['statusProposicao']
        ) if self.data.get("statusProposicao", None) else None
        self.uri_autores = self.data.get("uriAutores", None)
        self.descricao_tipo = self.data.get("descricaoTipo", None)
        self.ementa_detalhada = self.data.get("ementaDetalhada", None)
        self.keywords = self.data.get("keywords", '').split(',')
        self.uri_prop_principal = self.data.get("uriPropPrincipal", None)
        self.uri_prop_anterior = self.data.get("uriPropAnterior", None)
        self.uri_prop_posterior = self.data.get("uriPropPosterior", None)
        self.url_inteiro_teor = self.data.get("urlInteiroTeor", None)
        self.urn_final = self.data.get("urnFinal", None)
        self.texto = self.data.get("texto", None)
        self.justificativa = self.data.get("justificativa", None)

    def __str__(self):
        return '{} {}/{}'.format(self.sigla_tipo, self.numero, self.ano)


class Votacao(Model):
    """
    {
        "aprovacao": 0,
        "data": "string",
        "dataHoraRegistro": "string",
        "descricao": "string",
        "id": "string",
        "proposicaoObjeto": "string",
        "siglaOrgao": "string",
        "uri": "string",
        "uriEvento": "string",
        "uriOrgao": "string",
        "uriProposicaoObjeto": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.id = self.data['id']
        self.aprovacao = self.data['aprovacao']
        self.data = self.get_date(self.data['data'], DATE_FORMAT)
        self.data_hora_registro = self.get_data(self.data['dataHoraRegistro'])
        self.descricao = self.data['descricao']
        self.id = self.data['id']
        self.proposicao_objeto = self.data['proposicaoObjeto']
        self.sigla_orgao = self.data['siglaOrgao']
        self.uri = self.data['uri']
        self.uri_evento = self.data['uriEvento']
        self.uriOrgao = self.data['uriOrgao']
        self.uri_proposicao_object = self.data['uriProposicaoObjeto']

    def __str__(self):
        return self.descricao

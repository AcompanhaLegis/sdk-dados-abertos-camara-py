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


class DespesaDeputado(Model):
    """
    {
      "ano": 0,
      "cnpjCpfFornecedor": "string",
      "codDocumento": 0,
      "codLote": 0,
      "codTipoDocumento": 0,
      "dataDocumento": "string",
      "mes": 0,
      "nomeFornecedor": "string",
      "numDocumento": "string",
      "numRessarcimento": "string",
      "parcela": 0,
      "tipoDespesa": "string",
      "tipoDocumento": "string",
      "urlDocumento": "string",
      "valorDocumento": 0,
      "valorGlosa": 0,
      "valorLiquido": 0
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.ano = data['ano']
        self.cnpj_cpf_fornecedor = data['cnpjCpfFornecedor']
        self.cod_document = data['codDocumento']
        self.cod_lote = data['codLote']
        self.cod_tipo_documento = data['codTipoDocumento']
        self.data_documento = self.get_date(data['dataDocumento'], DATE_FORMAT)
        self.mes = data['mes']
        self.nome_fornecedor = data['nomeFornecedor']
        self.num_documento = data['numDocumento']
        self.num_ressarcimento = data['numRessarcimento']
        self.parcela = data['parcela']
        self.tipo_despesa = data['tipoDespesa']
        self.tipo_documento = data['tipoDocumento']
        self.url_documento = data['urlDocumento']
        self.valor_documento = data['valorDocumento']
        self.valor_glosa = data['valorGlosa']
        self.valor_liquido = data['valorLiquido']

    def __str__(self):
        return 'Despesa em {} dia {} valor: R$ {}'.format(
            self.nome_fornecedor,
            self.data['dataDocumento'],
            self.valor_liquido)


class DiscursoDeputado(Model):
    """
    {
      "dataHoraFim": "string",
      "dataHoraInicio": "string",
      "faseEvento": {
        "dataHoraFim": "string",
        "dataHoraInicio": "string",
        "titulo": "string"
      },
      "keywords": "string",
      "sumario": "string",
      "tipoDiscurso": "string",
      "transcricao": "string",
      "uriEvento": "string",
      "urlAudio": "string",
      "urlTexto": "string",
      "urlVideo": "string"
    }
    """

    def __init__(self, data):
        super().__init__(data)
        self.data_hora_fim = self.get_date(data['dataHoraFim'])
        self.data_hora_inicio = self.get_date(data['dataHoraInicio'])
        self.fase_evento = data['faseEvento']
        self.keywords = data['keywords']
        self.sumario = data['sumario']
        self.tipo_discurso = data['tipoDiscurso']
        self.transcricao = data['transcricao']
        self.uri_evento = data['uriEvento']
        self.url_audio = data['urlAudio']
        self.url_text = data['urlTexto']
        self.url_video = data['urlVideo']

    def __str__(self):
        return 'Discurso dia {}'.format(self.data_hora_inicio)


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
            self.andar=data.get('andar', '')
            self.nome=data.get('nome', '')
            self.predio=data.get('predio', '')
            self.sala=data.get('sala', '')

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
        self.apelido=data['apelido']
        self.cod_tipo_orgao=data['codTipoOrgao']
        self.id=data['id']
        self.nome=data['nome']
        self.nome_publicacao=data['nomePublicacao']
        self.sigla=data['sigla']
        self.tipo_orgao=data['tipoOrgao']
        self.uri=data['uri']

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
        self.data=data
        self.data_hora_fim=self.get_date(data['dataHoraFim'])
        self.data_hora_inicio=self.get_date(data['dataHoraInicio'])
        self.descricao=data['descricao']
        self.descricao_tipo=data['descricaoTipo']
        self.id=data['id']
        self.local_camara=LocalCamara(data['localCamara'])
        self.local_externo=data['localExterno']
        self.orgaos=[Orgao(o) for o in data['orgaos']]
        self.situacao=data['situacao']
        self.uri=data['uri']
        self.url_registro=data['urlRegistro']

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
        self.id=data['id']
        self.id_legislatura=data['idLegislatura']
        self.titulo=data['titulo']
        self.uri=data['uri']

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
        self.data_fim=self.get_date(
            data.get('dataFim', None), DATE_FORMAT)
        self.data_inicio=self.get_date(
            data.get('dataInicio', None), DATE_FORMAT)
        self.id=data['id']
        self.uri=data['uri']

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
        self.id=data['id']
        self.nome=data['nome']
        self.sigla=data['sigla']
        self.uri=data['uri']

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
        self.data_hora=self.get_date(data['dataHora'], DATE_FORMAT)
        self.sequencia=data['sequencia']
        self.sigla_orgao=data['siglaOrgao']
        self.uri_orgao=data['uriOrgao']
        self.regime=data['regime']
        self.descricao_tramitacao=data['descricaoTramitacao']
        self.cod_tipo_tramitacao=data['codTipoTramitacao']
        self.cod_situacao=data['codSituacao']
        self.despacho=data['despacho']
        self.url=data['url']
        self.ambito=data['ambito']

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
        self.id=data['id']
        self.uri=data['uri']
        self.sigla_tipo=data['siglaTipo']
        self.cod_tipo=data['codTipo']
        self.numero=data['numero']
        self.ano=data['ano']
        self.ementa=data['ementa']
        self.data_apresentacao=self.get_date(
            data.get('dataApresentacao'))
        self.uri_orgao_numerador=data.get('uriOrgaoNumerador', None)
        self.status_proposicao=StatusProposicao(
            data['statusProposicao']
        ) if data.get("statusProposicao", None) else None
        self.uri_autores=data.get("uriAutores", None)
        self.descricao_tipo=data.get("descricaoTipo", None)
        self.ementa_detalhada=data.get("ementaDetalhada", None)
        self.keywords=data.get("keywords", '').split(',')
        self.uri_prop_principal=data.get("uriPropPrincipal", None)
        self.uri_prop_anterior=data.get("uriPropAnterior", None)
        self.uri_prop_posterior=data.get("uriPropPosterior", None)
        self.url_inteiro_teor=data.get("urlInteiroTeor", None)
        self.urn_final=data.get("urnFinal", None)
        self.texto=data.get("texto", None)
        self.justificativa=data.get("justificativa", None)

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
        self.id=data['id']
        self.aprovacao=data['aprovacao']
        self.data=self.get_date(data['data'], DATE_FORMAT)
        self.data_hora_registro=self.get_data(data['dataHoraRegistro'])
        self.descricao=data['descricao']
        self.id=data['id']
        self.proposicao_objeto=data['proposicaoObjeto']
        self.sigla_orgao=data['siglaOrgao']
        self.uri=data['uri']
        self.uri_evento=data['uriEvento']
        self.uriOrgao=data['uriOrgao']
        self.uri_proposicao_object=data['uriProposicaoObjeto']

    def __str__(self):
        return self.descricao

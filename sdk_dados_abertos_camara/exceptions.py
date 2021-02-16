class CamaraAPIException(Exception):
    """
    Exception raised when the API returns a > 299 status code.
    """

    def __init__(self, status, endpoint='/'):
        self.message = 'API Dados Abertos da Camara returned an error: '\
            '[{}] on endpoint [{}]'.format(status, endpoint)
        super().__init__()


class CamaraAPIInvalidID(Exception):
    """
    Exception raised when the API returns a > 299 status code.
    """

    def __init__(self, endpoint):
        self.message = 'API Dados Abertos da Camara'\
            'invalid ID for: [{}]'.format(endpoint)
        super().__init__()

class CamaraAPIException(Exception):
    """
    Exception raised when the API returns a > 299 status code.
    """

    def __init__(self, status, endpoint='/'):
        self.message = 'API Dados Abertos da Camara returned an error: '\
                '[{}] on endpoint [{}]'.format(status, endpoint)
        super(CamaraAPIException, self).__init__(self.message)

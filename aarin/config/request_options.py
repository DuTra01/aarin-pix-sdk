from requests.api import head
from .config import Config
from json.encoder import JSONEncoder

from requests import request

class Auth:
    def __init__(self, empresaId, senha, escopo) -> None:
        self.empresaId = empresaId
        self.senha = senha
        self.escopo = escopo

class Token:
    __access_token  = None
    __refresh_token = None

    def __init__(self, auth: Auth) -> None:
        self.auth = auth
        self.headers = {'Content-Type': 'application/json'}
    
    @property
    def access_token(self):
        return self.__access_token
    
    @property
    def refresh_token(self):
        return self.__refresh_token
    
    def create(self):
        data    = JSONEncoder().encode(self.auth.__dict__)
        result  = request('POST', Config().api_base_url + '/v1/oauth/token', data=data, headers=self.headers)
        self.parse(result)

    def refresh(self):
        if self.__refresh_token is not None:
            data = JSONEncoder().encode({'refreshToken': self.__refresh_token})
            result  = request('POST', Config().api_base_url + '/v1/oauth/refresh', data=data, headers=self.headers)
            self.parse(result)
    
    def parse(self, result):
        if result.status_code == 200:
            result = result.json()
            self.__access_token  = result['accessToken']
            self.__refresh_token = result['refreshToken']

class RequestOptions:
    __access_token = None
    __connection_timeout = None
    __custom_headers = None
    __max_retries = None

    def __init__(self, access_token=None,
                 connection_timeout=60.0,
                 custom_headers=None,
                 max_retries=3) -> None:

        if access_token is not None:
            self.access_token = access_token
        if connection_timeout is not None:
            self.connection_timeout = connection_timeout
        if custom_headers is not None:
            self.custom_headers = custom_headers
        if max_retries is not None:
            self.max_retries = max_retries

        self.__config = Config()
    
    def get_headers(self):
        headers = {
                'Authorization': 'Bearer ' + self.__access_token,
                'User-Agent': self.__config.user_agent,
                'Accept': self.__config.mime_json
            }

        if self.__custom_headers is not None:
            headers.update(self.__custom_headers)

        return headers
    
    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        if not isinstance(value, str):
            raise ValueError('Param access_token must be a String')
        self.__access_token = value

    @property
    def connection_timeout(self):
        return self.__connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, value):
        if not isinstance(value, float):
            raise ValueError('Param connection_timeout must be a Float')
        self.__connection_timeout = value

    @property
    def custom_headers(self):
        return self.__custom_headers

    @custom_headers.setter
    def custom_headers(self, value):
        if not isinstance(value, dict):
            raise ValueError('Param custom_headers must be a Dictionary')
        self.__custom_headers = value


    @property
    def max_retries(self):
        return self.__max_retries

    @max_retries.setter
    def max_retries(self, value):
        if not isinstance(value, int):
            raise ValueError('Param max_retries must be an Integer')
        self.__max_retries = value
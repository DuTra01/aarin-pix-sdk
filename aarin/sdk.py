from .config import RequestOptions
from .http import HttpClient
from .resources import Collection, BankAccount, DestinationAccount, Pix

class SDK:
    def __init__(self, access_token, contaBancariaIdconta=None, http_client=None, request_options=None) -> None:

        self.http_client = http_client
        if http_client is None:
            self.http_client = HttpClient()

        self.request_options = request_options
        if request_options is None:
            self.request_options = RequestOptions()

        self.request_options.access_token = access_token
        if contaBancariaIdconta is not None and isinstance(contaBancariaIdconta, str):
            request_options.custom_headers = {'X-ContaBancariaId': contaBancariaIdconta}
            
    def collection(self, request_options=None):
        return Collection(request_options is not None and request_options
        or self.request_options, self.http_client)

    def bank_account(self, request_options=None):
        return BankAccount(request_options is not None and request_options
        or self.request_options, self.http_client)
    
    def dst_account(self, request_options=None):
        return DestinationAccount(request_options is not None and request_options
        or self.request_options, self.http_client)
    
    def pix(self, request_options=None):
        return Pix(request_options is not None and request_options
        or self.request_options, self.http_client)
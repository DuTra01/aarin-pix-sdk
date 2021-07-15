from aarin.core import Base

class DestinationAccount(Base):
    def __init__(self, request_options, http_client):
        super().__init__(request_options, http_client)
    
    def create(self, data_target_account, contaBancariaId=None):
        if isinstance(contaBancariaId, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': contaBancariaId}
        
        if not isinstance(data_target_account, dict):
            raise ValueError('Param data_target_account must be dict')

        return self._post('/v1/contas-destino/', data=data_target_account)
    
    def search(self, account_id=None, filters=None, contaBancariaId=None):
        if isinstance(contaBancariaId, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': contaBancariaId}
        
        if isinstance(account_id, str):
            return self._get('/v1/contas-destino/' + str(account_id))

        return self._get('/v1/contas-destino/', filters=filters)
    
    def delete(self, account_id, contaBancariaId=None):
        if isinstance(contaBancariaId, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': contaBancariaId}
        
        if not isinstance(account_id, str):
            raise ValueError('Param data_target_account must be string')
        
        return self._delete('/v1/contas-destino/' + str(account_id))
    
    def update(self, account_id, data_target_account, contaBancariaId=None):
        if isinstance(contaBancariaId, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': contaBancariaId}
        
        if not isinstance(data_target_account, str):
            raise ValueError('Param data_target_account must be dict')
        
        if not isinstance(account_id, str):
            raise ValueError('Param data_target_account must be string')
        
        return self._put('/v1/contas-destino/' + str(account_id), data=data_target_account)
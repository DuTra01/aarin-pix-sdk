from aarin.core import Base

class Pix(Base):
    def __init__(self, request_options, http_client):
        super().__init__(request_options, http_client)

    
    def pix_transfer_with_destination(self, transfer_obj, bank_account_id=None):
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        if not isinstance(transfer_obj, dict):
            raise ValueError('Param transfer_obj must be a dict')
        
        return self._post('/v1/pix/destino', data=transfer_obj)
    
    def pix_transfer_manual(self, transfer_obj, bank_account_id=None):
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        if not isinstance(transfer_obj, dict):
            raise ValueError('Param transfer_obj must be a dict')
        
        return self._post('/v1/pix', data=transfer_obj)

    def search_pix(self, pixId, bank_account_id=None):
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        if not isinstance(pixId, str):
            raise ValueError('Param pixId must be a string')
        
        return self._get('/v1/pix/' + str(pixId))
    
    def search_pix_received(self, filters=None, bank_account_id=None):
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        return self._get('/v1/pix/', filters=filters)
    
    def request_pix_back(self, pixId, customer_id, amount_obj, bank_account_id=None):
        if not isinstance(pixId, str):
            raise ValueError('Param pixId must be a string')
        
        if not isinstance(customer_id, str):
            raise ValueError('Param customer_id must be a string')
        
        if not isinstance(amount_obj, str):
            raise ValueError('Param amount_obj must be a dict')
        
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        return self._put('/v1/pix/' + str(pixId) + '/devolucao/' + str(customer_id), data=amount_obj)
    
    def search_pix_back(self, pixId, customer_id, bank_account_id=None):
        if not isinstance(pixId, str):
            raise ValueError('Param pixId must be a string')
        
        if not isinstance(customer_id, str):
            raise ValueError('Param customer_id must be a string')
        
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        return self._get('/v1/pix/' + str(pixId) + '/devolucao/' + str(customer_id))
    
    def search_pix_transfer_received(self, transfer_pix_id=None, filters=None, bank_account_id=None):
        if isinstance(bank_account_id, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': bank_account_id}
        
        if isinstance(transfer_pix_id, str):
            return self._get('/v1/pix/transferencias/' + str(transfer_pix_id))
        
        return self._get('/v1/pix/transferencias/', filters=filters)
#!/usr/bin/env python3

from  aarin.core import Base

class BankAccount(Base):
    def __init__(self, request_options, http_client):
        super().__init__(request_options, http_client)

    def search(self, account_id=None):
        if isinstance(account_id, str):
            return self._get('/v1/contas-bancarias/' + str(account_id))
            
        return self._get('/v1/contas-bancarias')
    
    def create(self, data_obj):
        if not isinstance(data_obj, dict):
            raise ValueError('Param data_obj must be a Dictionary')

        return self._post('/v1/contas-bancarias', data=data_obj)
    
    def update(self, account_id, data_obj):
        if not isinstance(data_obj, dict):
            raise ValueError('Param data_obj must be a Dictionary')

        if not isinstance(account_id, str):
            raise ValueError('Param account_id must be a Dictionary')

        return self._put('/v1/contas-bancarias/' + str(account_id), data=data_obj)
    
    def delete(self, account_id=None):
        if not isinstance(account_id, str):
            raise ValueError('Param account_id must be a Dictionary')

        return self._delete('/v1/contas-bancarias/' + str(account_id))
    
    def balance(self, contaBancariaId=None):
        if isinstance(contaBancariaId, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': contaBancariaId}

        return self._get('/v1/contas-bancarias/saldo')
    
    def statement(self, inicio=None, fim=None, contaBancariaId=None):
        filters = None
        if isinstance(inicio, str) and isinstance(fim, str):
            filters = {'inicio': inicio, 'fim': fim}

        if isinstance(contaBancariaId, str):
            self.request_options.custom_headers = {'X-ContaBancariaId': contaBancariaId}

        return self._get('/v1/contas-bancarias/extrato', filters=filters)
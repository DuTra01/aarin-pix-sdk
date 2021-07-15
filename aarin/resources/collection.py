#!/usr/bin/env python3

from  aarin.core import Base

class Collection(Base):
    def __init__(self, request_options, http_client):
        Base.__init__(self, request_options, http_client)

    def create(self, cob_obj):
        if not isinstance(cob_obj, dict):
            raise ValueError('Param cob_object must be a Dictionary')

        return self._post(uri='/v1/cob', data=cob_obj)

    def search(self, cob_id=None):
        if isinstance(cob_id, str):
            return self._get(uri='/v1/cob/' + str(cob_id))

        return self._get(uri='/v1/cob/')

    def edit(self, cob_id, cob_obj):
        if not isinstance(cob_id, str):
            raise ValueError('Param cob_id must be a string')

        if not isinstance(cob_obj, dict):
            raise ValueError('Param cob_obj must be a dict')

        return self._patch(uri='/v1/cob/' + str(cob_id), data=cob_obj)
    
    def invalidate(self, cob_id):
        if not isinstance(cob_id, str):
            raise ValueError('Param cob_id must be a string')

        return self._delete(uri='/v1/cob/' + str(cob_id))
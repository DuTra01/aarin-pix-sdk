#!/usr/bin/env python3
import platform

class Config:
    __api_base_url = 'https://pix.aarin.com.br/api'
    __mime_json = 'application/json'
    __mime_form = 'application/x-www-form-urlencoded'

    def __init__(self):
        self.__version = '1.0.0'
        self.__user_agent = 'Pix Aarin Python SDK v' + self.__version

    @property
    def version(self):
        return self.__version

    @property
    def user_agent(self):
        return self.__user_agent

    @property
    def api_base_url(self):
        return self.__api_base_url

    @property
    def mime_json(self):
        return self.__mime_json

    @property
    def mime_form(self):
        return self.__mime_form

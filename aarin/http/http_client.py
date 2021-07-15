#!/usr/bin/env python3
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

class HttpClient:

    @staticmethod
    def __get_session(max_retries):
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        http = requests.Session()
        http.mount('https://', HTTPAdapter(max_retries=retry_strategy))
        return http
    
    def get(self, url, headers, params=None, timeout=None, maxretries=None):
        with self.__get_session(maxretries) as session:
            api_result = session.get(url, params=params, headers=headers, timeout=timeout)
            response = {
                'status': api_result.status_code,
                'response': api_result.json() if len(api_result.content) > 0 else {}
            }

        return response

    def post(self, url, headers, data=None, params=None, timeout=None, maxretries=None):
        with self.__get_session(maxretries) as session:
            api_result = session.post(url, params=params, data=data,
            headers=headers, timeout=timeout)
            response = {
                'status': api_result.status_code,
                'response': api_result.json() if len(api_result.content) > 0 else {}
            }

        return response

    def put(self, url, headers, data=None, params=None, timeout=None, maxretries=None):
        with self.__get_session(maxretries) as session:
            api_result = session.put(url, params=params, data=data,
            headers=headers, timeout=timeout)
            response = {
                'status': api_result.status_code,
                'response': api_result.json() if len(api_result.content) > 0 else {}
            }

        return response
    
    def patch(self, url, headers, data=None, params=None, timeout=None, maxretries=None):
        with self.__get_session(maxretries) as session:
            api_result = session.patch(url, data=data, params=params, headers=headers, timeout=timeout)
            response = {
                'status': api_result.status_code,
                'response': api_result.json() if len(api_result.content) > 0 else {}
            }

        return response

    def delete(self, url, headers, params=None, timeout=None, maxretries=None):
        with self.__get_session(maxretries) as session:
            api_result = session.delete(url, params=params, headers=headers, timeout=timeout)
            response = {
                'status': api_result.status_code,
                'response': api_result.json() if len(api_result.content) > 0 else {}
            }

        return response
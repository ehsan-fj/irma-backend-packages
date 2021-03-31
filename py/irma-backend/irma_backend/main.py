"""
This module is used to handle communication to irma server.
"""

import requests
from enum import Enum


class AuthenticationMethod(Enum):
    TOKEN = 'token'
    HMAC = 'hmac'
    PUBLICKEY = 'publickey'


class IrmaBackend:
    """

    """

    def __init__(self, server_url, debug=False, server_token=None):
        """
        """
        self._server_url = server_url
        self._server_token = server_token
        self._debug = debug

    def __send_request(self, endpoint, data, method='POST', headers=None):
        """

        :param endpoint:
        :param headers:
        :return:
        """
        if not headers:
            headers = {}

        if self._options.get('server_token'):
            headers['Authorization'] = self._options.get('server_token')

        response = requests.request(
            method,
            self._server_url+'/'+endpoint,
            data=data,
            headers=headers,
        )

        if response.status_code != requests.codes.ok:
            response.raise_for_status()

        return response

    def start_session(self, request):
        """

        :param request:
        :return:
        """
        headers = {}

        if type(request) is str:
            headers['Content-Type'] = 'text/plain'
        else:
            headers['Content-Type'] = 'application/json'

        response = self.__send_request('session', request, headers=headers)
        return response.json()

import requests
import urllib

from .exception import (AppAnnieException, AppAnnieBadRequestException,
                        AppAnnieNotFoundException,
                        AppAnnieUnauthorizedException,
                        AppAnnieRateLimitException)


class HttpClient(object):
    ENDPOINT = 'https://api.appannie.com/v1.2'

    def __init__(self, api_key):
        self.api_key = api_key

    def get_url(self, uri, data={}):
        url = self.ENDPOINT + uri
        if data:
            # urlencode parameters deterministically:
            sorted_values = sorted(data.items(), key=lambda val: val[0])
            url = url + '?' + urllib.urlencode(sorted_values)
        return url

    def _get_default_headers(self):
        return {
            'Authorization': 'Bearer ' + self.api_key,
            'Accept': 'application/json',
        }

    def request(self, uri, data={}):
        url = self.get_url(uri, data)
        headers = self._get_default_headers()

        try:
            response = requests.get(url, headers=headers).json()
            if self.is_error(response):
                raise self.get_exception_from_response(response)
            return response
        except requests.exceptions.RequestException as e:
            raise AppAnnieException(e.message)
        except ValueError:
            raise AppAnnieException("Empty data returned by AppAnnie.")

    def is_error(self, response):
        return bool(response.get('error', False))

    def get_exception_from_response(self, response):
        code = response['code']
        message = response['error']
        if code == AppAnnieBadRequestException.ERROR_CODE:
            return AppAnnieBadRequestException(message)
        if code == AppAnnieUnauthorizedException.ERROR_CODE:
            return AppAnnieUnauthorizedException(message)
        if code in [AppAnnieNotFoundException.ERROR_CODE, 405, 403]:
            return AppAnnieNotFoundException(message)
        if code == AppAnnieRateLimitException.ERROR_CODE:
            return AppAnnieRateLimitException(message)
        return AppAnnieException(message)

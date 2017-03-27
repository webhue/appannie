from __future__ import absolute_import

import unittest2
import requests
import mock

from appannie.http import HttpClient
from appannie.exception import (AppAnnieException, AppAnnieRateLimitException,
                                AppAnnieNotFoundException)


class TestHttp(unittest2.TestCase):
    API_KEY = 'dummy'
    client = HttpClient(API_KEY)

    def test_default_headers(self):
        headers = self.client._get_default_headers()
        self.assertIn('Authorization', headers)
        self.assertTrue(self.API_KEY in headers['Authorization'])

    def test_get_url(self):
        uri = '/some/uri'
        data = {
            'param1': 'val1',
            'param2': 'val2',
        }

        url = self.client.get_url(uri)
        self.assertTrue(url.startswith(HttpClient.ENDPOINT))
        self.assertTrue(url.endswith('/some/uri'))
        self.assertFalse('?' in url)

        url = self.client.get_url(uri, data)
        self.assertTrue(url.startswith(HttpClient.ENDPOINT))
        self.assertTrue(url.endswith('/some/uri?param1=val1&param2=val2'))
        self.assertTrue('?' in url)

    def test_is_error(self):
        response = {'error': 'some error'}
        result = self.client.is_error(response)
        self.assertEqual(result, True)

        response = {'param': 'val'}
        result = self.client.is_error(response)
        self.assertEqual(result, False)

    def test_get_exception_from_response(self):
        msg = 'some error'

        # general case for unknown code:
        code = 999
        exception = self.client.get_exception_from_response({'error': msg,
                                                             'code': code})
        self.assertTrue(issubclass(exception.__class__, AppAnnieException))
        self.assertEqual(exception.message, msg)
        self.assertEqual(exception.ERROR_CODE, AppAnnieException.ERROR_CODE)

        # general case for known code:
        code = AppAnnieRateLimitException.ERROR_CODE
        exception = self.client.get_exception_from_response({'error': msg,
                                                             'code': code})
        self.assertTrue(isinstance(exception, AppAnnieRateLimitException))
        self.assertEqual(exception.message, msg)
        self.assertEqual(exception.ERROR_CODE, code)

        # some 'not found' exceptions:
        code = 405
        exception = self.client.get_exception_from_response({'error': msg,
                                                             'code': code})
        self.assertTrue(isinstance(exception, AppAnnieNotFoundException))

        code = 403
        exception = self.client.get_exception_from_response({'error': msg,
                                                             'code': code})
        self.assertTrue(isinstance(exception, AppAnnieNotFoundException))

    @mock.patch('appannie.http.requests.get')
    def test_request(self, mock_get):
        uri = '/some/uri'
        data = {'breakdowns': 'b1+b2'}
        expected_result = {'code': 200,
                           'list': [{'param:': 'vals'}, {'param2': 'vals2'}]}
        expected_url = self.client.get_url(uri, data)
        expected_headers = self.client._get_default_headers()

        response = mock.Mock()
        response.json.return_value = expected_result
        mock_get.return_value = response
        result = self.client.request(uri, data)
        self.assertEqual(expected_result, result)
        mock_get.assert_called_once_with(expected_url,
                                         headers=expected_headers)

    @mock.patch('appannie.http.requests.get')
    def test_request_error(self, mock_get):
        uri = '/some/uri'

        response = mock.Mock()
        response.json.side_effect = ValueError("")
        mock_get.return_value = response
        with self.assertRaises(AppAnnieException):
            self.client.request(uri)

        mock_get.reset_mock()
        mock_get.side_effect = requests.exceptions.RequestException
        with self.assertRaises(AppAnnieException):
            self.client.request(uri)

    @mock.patch('appannie.http.requests.get')
    def test_request_response_error(self, mock_get):
        uri = '/some/uri'
        expected_message = 'error message'
        expected_result = {'code': 500,
                           'error': expected_message}

        response = mock.Mock()
        response.json.return_value = expected_result
        mock_get.return_value = response
        with self.assertRaises(AppAnnieException) as context:
            self.client.request(uri)
            self.assertEqual(context.exception.message, expected_message)

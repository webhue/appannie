from __future__ import absolute_import

import unittest2
import requests

from mock import patch

from appannie.paginator import Paginator
from appannie.http import HttpClient


class TestPaginator(unittest2.TestCase):
    API_KEY = 'api key'
    URI = '/some/uri'
    UNION_KEY = 'unionkey'

    @patch.object(HttpClient, 'request')
    def _get_union_result(self, responses, mock_request):
        mock_request.side_effect = responses
        client = HttpClient(self.API_KEY)
        paginator = Paginator(client, self.URI, union_key=self.UNION_KEY)
        return paginator.all()

    def test_union(self):
        # missing union key parameter error:
        client = HttpClient(self.API_KEY)
        paginator = Paginator(client, self.URI)
        with self.assertRaises(ValueError):
            paginator.all()

        # missing union key in response:
        responses = [
            {'code': 200,
             self.UNION_KEY: [{'param:': 'vals'}, {'param2': 'vals2'}]},
            {'code': 200,
             self.UNION_KEY + 'other': [{'param3:': 'vals3'}, {'param4': 'vals4'}]},
        ]
        expected_result = [{'param:': 'vals'}, {'param2': 'vals2'}]
        result = self._get_union_result(responses)
        self.assertEqual(result, expected_result)

        # TODO: check when no pages in result
        # TODO: check when a single page exists???
        # TODO: check the case when page_num is not returned
        # TODO: check when empty result
        # TODO: check the actual union (when everything is fine, and multiple pages)

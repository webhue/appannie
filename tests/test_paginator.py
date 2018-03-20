from __future__ import absolute_import

import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from appannie.paginator import Paginator
from appannie.http import HttpClient


class TestPaginator(unittest.TestCase):
    API_KEY = 'api key'
    URI = '/some/uri'
    UNION_KEY = 'unionkey'

    @patch.object(HttpClient, 'request')
    def _get_union_result(self, responses, mock_request):
        mock_request.side_effect = responses
        client = HttpClient(self.API_KEY)
        paginator = Paginator(client, self.URI, union_key=self.UNION_KEY)
        return paginator.all(), mock_request

    def _generate_response(self, rangestart=1, rangeend=3,
                           union_key=UNION_KEY, code=200, page_index=0,
                           **kwargs):
        listresult = []
        for index in range(rangestart, rangeend):
            strindex = str(index)
            listresult.append({
                'param' + strindex: 'val' + strindex,
                'otherparam' + strindex: 'otherval' + strindex,
            })
        response = {
            'code': code,
            'page_index': page_index,
            union_key: listresult
        }
        response.update(kwargs)
        return response

    def test_union(self):
        # missing union key parameter error:
        client = HttpClient(self.API_KEY)
        paginator = Paginator(client, self.URI)
        with self.assertRaises(ValueError):
            paginator.all()

        # invalid/missing union key in response:
        responses = [
            self._generate_response(1, 2, page_num=2, page_index=0),
            self._generate_response(3, 6, page_num=2, page_index=1,
                                    union_key=self.UNION_KEY + 'other'),
        ]
        expected_result = self._generate_response(1, 2).get(self.UNION_KEY)
        result, mock_request = self._get_union_result(responses)
        self.assertEqual(result, expected_result)

        # no pages in result:
        responses = [
            self._generate_response(1, 1, page_num=1),
        ]
        result, mock_request = self._get_union_result(responses)
        self.assertEqual(result, [])

        # page_num is not returned:
        responses = [
            self._generate_response(1, 1),
        ]
        result, mock_request = self._get_union_result(responses)
        self.assertEqual(result, [])

        # single page response:
        page_response = self._generate_response(1, 2, page_num=1)
        expected_result = page_response.get(self.UNION_KEY)
        result, mock_request = self._get_union_result([page_response])
        self.assertEqual(result, expected_result)

        # general case:
        page_num = 3
        responses = []
        for page_index in range(0, page_num):
            # making param names consecutive we can generate the expected
            # result easier
            response = self._generate_response(1, 3, page_num=page_num,
                                               page_index=page_index)
            responses.append(response)

        expected_result = self._generate_response(1, 3).get(self.UNION_KEY)
        expected_result = expected_result * page_num

        result, mock_request = self._get_union_result(responses)
        self.assertEqual(result, expected_result)
        self.assertEqual(mock_request.call_count, page_num)

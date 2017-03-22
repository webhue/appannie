from appannie.util import format_request_data
from .app import App
from .keyword import Keyword


class Store(object):
    RANKING_ENDPOINT = '/apps/{market}/ranking'
    PACKAGE_CODE_TO_ID_ENDPOINT = '/apps/{market}/package-codes2ids'

    def __init__(self, http_client, paginator, market):
        self.http_client = http_client
        self.paginator = paginator
        self.market = market

    def app(self, product_id):
        return App(self.http_client, self.paginator,
                   self.market, product_id)

    def keyword(self, product_id=None):
        return Keyword(self.http_client, self.market, product_id)

    def ranking(self, countries, categories, **kwargs):
        data = format_request_data(countries=countries, categories=categories,
                                   **kwargs)
        uri = self.RANKING_ENDPOINT.format(market=self.market)
        return self.http_client.request(uri, data).get('products')

    def package_code_to_id(self, package_codes):
        if isinstance(package_codes, list):
            package_codes = u','.join(package_codes)
        data = {'package_codes': package_codes}
        uri = self.PACKAGE_CODE_TO_ID_ENDPOINT.format(market=self.market)
        return self.http_client.request(uri, data).get('items')

from appannie.util import format_request_data


class FeaturesMetadata(object):
    CATEGORIES_ENDPOINT = '/meta/feature/categories'
    TYPES_ENDPOINT = '/meta/feature/types'

    def __init__(self, http_client, market):
        self.http_client = http_client
        self.market = market

    def categories(self, countries=None):
        data = format_request_data(market=self.market, countries=countries)
        r = self.http_client.request(self.CATEGORIES_ENDPOINT, data)
        return r.get('all_category_pages')

    def types(self):
        data = format_request_data(market=self.market)
        r = self.http_client.request(self.TYPES_ENDPOINT, data)
        return r.get('types')

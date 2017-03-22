from .store import StoreMetadata
from .features import FeaturesMetadata


class Metadata(object):
    COUNTRIES_ENDPOINT = '/meta/countries'
    MARKETS_ENDPOINT = '/meta/markets'
    CURRENCIES_ENDPOINT = '/meta/currencies'

    def __init__(self, http_client):
        self.http_client = http_client

    def countries(self):
        r = self.http_client.request(self.COUNTRIES_ENDPOINT)
        return r.get('country_list')

    def currencies(self):
        r = self.http_client.request(self.CURRENCIES_ENDPOINT)
        return r.get('currency_list')

    def markets(self):
        r = self.http_client.request(self.MARKETS_ENDPOINT)
        return r.get('verticals')

    def verticals(self):
        return {vertical['vertical_code']: vertical
                for vertical in self.markets()}

    def store(self, market=None):
        return StoreMetadata(self, self.http_client, market)

    def features(self, market):
        return FeaturesMetadata(self.http_client, market)

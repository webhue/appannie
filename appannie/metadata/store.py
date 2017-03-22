class StoreMetadata(object):
    CATEGORIES_ENDPOINT = '/meta/apps/{market}/categories'
    DEVICES_ENDPOINT = '/meta/apps/{market}/devices'
    FEEDS_ENDPOINT = '/meta/apps/{market}/feeds'

    def __init__(self, meta, http_client, market=None):
        self.meta = meta
        self.http_client = http_client
        self.market = market

    def all(self):
        return self.meta.verticals().get('apps')

    def _format_uri(self, uri):
        if not self.market:
            raise ValueError("Store/market not specified")
        return uri.format(market=self.market)

    def categories(self):
        uri = self._format_uri(self.CATEGORIES_ENDPOINT)
        return self.http_client.request(uri).get('category_labels')

    def devices(self):
        uri = self._format_uri(self.DEVICES_ENDPOINT)
        return self.http_client.request(uri).get('devices')

    def feeds(self):
        uri = self._format_uri(self.FEEDS_ENDPOINT)
        return self.http_client.request(uri).get('feeds')

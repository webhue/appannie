from appannie.util import format_request_data


class Keyword(object):
    EXPLORER_ENDPOINT = '/apps/{market}/keywords/explorer'
    RANKED_ENDPOINT = '/apps/{market}/app/{product_id}/keywords/ranked'
    PERFORMANCE_ENDPOINT = '/apps/{market}/app/{product_id}/keywords/ranks'

    def __init__(self, http_client, market, product_id=None):
        self.http_client = http_client
        self.market = market
        self.product_id = product_id

    def _format_uri(self, uri):
        if not self.product_id:
            raise ValueError("Product id not specified")
        return uri.format(market=self.market, product_id=self.product_id)

    def explore(self, country, device, date, keyword):
        data = format_request_data(keyword=keyword, date=date, country=country,
                                   device=device)
        uri = self.EXPLORER_ENDPOINT.format(market=self.market)
        return self.http_client.request(uri, data)

    def ranked(self, country, device, date):
        data = format_request_data(date=date, country=country, device=device)
        uri = self._format_uri(self.RANKED_ENDPOINT)
        return self.http_client.request(uri, data)

    def performance(self, country, device, start_date, end_date, keywords):
        data = format_request_data(keywords=keywords, start_date=start_date,
                                   end_date=end_date, country=country,
                                   device=device)
        uri = self._format_uri(self.PERFORMANCE_ENDPOINT)
        return self.http_client.request(uri, data)

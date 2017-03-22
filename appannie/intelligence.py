from .util import format_request_data


class Intelligence(object):
    RANKING_ENDPOINT = '/intelligence/apps/{market}/ranking'
    APP_HISTORY_ENDPOINT = '/intelligence/apps/{market}/app/{product_id}/history'
    PUBLISHER_RANKING_ENDPOINT = '/intelligence/apps/{market}/publisher-ranking'
    PUBLISHER_HISTORY_ENDPOINT = '/intelligence/apps/{market}/publisher/{publisher_id}/history'

    USAGE_RANKING_ENDPOINT = '/intelligence/apps/{market}/usage-ranking'
    USAGE_HISTORY_ENDPOINT = '/intelligence/apps/{market}/app/{product_id}/usage-history'
    USER_RETENTION_ENDPOINT = '/intelligence/apps/{market}/app/{product_id}/user-retention'

    CROSS_APP_USAGE_ENDPOINT = '/intelligence/apps/{market}/app/{product_id}/cross_app_usage'
    DEMOGRAPHICS_ENDPOINT = '/intelligence/apps/{market}/app/{product_id}/demographics'

    def __init__(self, http_client, paginator, market):
        self.http_client = http_client
        self.paginator = paginator
        self.market = market

    def app_ranking(self, countries, device, categories, **kwargs):
        data = format_request_data(countries=countries, categories=categories,
                                   device=device, **kwargs)
        uri = self.RANKING_ENDPOINT.format(market=self.market)
        return self.http_client.request(uri, data)

    def app_history(self, product_id, countries, feeds, **kwargs):
        data = format_request_data(countries=countries, feeds=feeds, **kwargs)
        uri = self.APP_HISTORY_ENDPOINT.format(market=self.market,
                                               product_id=product_id)
        return self.http_client.request(uri, data)

    def publisher_ranking(self, countries, device, categories, **kwargs):
        data = format_request_data(countries=countries, categories=categories,
                                   device=device, **kwargs)
        uri = self.PUBLISHER_RANKING_ENDPOINT.format(market=self.market)
        return self.http_client.request(uri, data)

    def publisher_history(self, countries, categories, publisher_id, feeds,
                          **kwargs):
        data = format_request_data(countries=countries, categories=categories,
                                   feeds=feeds, **kwargs)
        uri = self.PUBLISHER_HISTORY_ENDPOINT.format(market=self.market,
                                                     publisher_id=publisher_id)
        return self.http_client.request(uri, data)

    def usage_ranking(self, countries, device, categories, **kwargs):
        data = format_request_data(countries=countries, categories=categories,
                                   device=device, **kwargs)
        uri = self.USAGE_RANKING_ENDPOINT.format(market=self.market)
        return self.http_client.request(uri, data)

    def usage_history(self, product_id, countries, **kwargs):
        data = format_request_data(countries=countries, **kwargs)
        uri = self.USAGE_HISTORY_ENDPOINT.format(market=self.market,
                                                 product_id=product_id)
        return self.http_client.request(uri, data)

    def user_retention(self, product_id, countries, **kwargs):
        data = format_request_data(countries=countries, **kwargs)
        uri = self.USER_RETENTION_ENDPOINT.format(market=self.market,
                                                  product_id=product_id)
        return self.http_client.request(uri, data)

    def cross_app_usage(self, product_id, countries, categories, **kwargs):
        data = format_request_data(countries=countries,
                                   categories=categories, **kwargs)
        uri = self.CROSS_APP_USAGE_ENDPOINT.format(market=self.market,
                                                   product_id=product_id)
        return self.http_client.request(uri, data)

    def demographics(self, product_id, countries, **kwargs):
        data = format_request_data(countries=countries, **kwargs)
        uri = self.DEMOGRAPHICS_ENDPOINT.format(market=self.market,
                                                product_id=product_id)
        return self.http_client.request(uri, data)

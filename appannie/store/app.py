from appannie.util import format_request_data, to_day


class App(object):
    PRODUCT_ENDPOINT = '/apps/{market}/app/{product_id}/details'
    FEATURED_ENDPOINT = '/apps/{market}/app/{product_id}/featured'
    FEATURED_HISTORY_ENDPOINT = '/apps/{market}/app/{product_id}/featured_history'
    REVIEWS_ENDPOINT = '/apps/{market}/app/{product_id}/reviews'
    RATINGS_ENDPOINT = '/apps/{market}/app/{product_id}/ratings'
    RANKS_ENDPOINT = '/apps/{market}/app/{product_id}/ranks'
    ADS_ENDPOINT = '/apps/{market}/app/{product_id}/ad_items'

    def __init__(self, http_client, paginator, market, product_id):
        self.http_client = http_client
        self.paginator = paginator
        self.market = market
        self.product_id = product_id

    def _format_uri(self, uri):
        return uri.format(market=self.market,
                          product_id=self.product_id)

    def _format_data(self, start_date, end_date, **kwargs):
        data = format_request_data(**kwargs)
        data['start_date'] = to_day(start_date)
        data['end_date'] = to_day(end_date)
        return data

    def details(self):
        uri = self._format_uri(self.PRODUCT_ENDPOINT)
        return self.http_client.request(uri).get('product')

    def ads(self, **kwargs):
        data = format_request_data(**kwargs)
        uri = self._format_uri(self.ADS_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='ad_items')

    def featured(self, start_date, end_date, **kwargs):
        data = self._format_data(start_date, end_date, **kwargs)
        uri = self._format_uri(self.FEATURED_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='daily_features')

    def featured_history(self, start_date, end_date, **kwargs):
        data = self._format_data(start_date, end_date, **kwargs)
        uri = self._format_uri(self.FEATURED_HISTORY_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='feature_history')

    def reviews(self, start_date, end_date, **kwargs):
        data = self._format_data(start_date, end_date, **kwargs)
        uri = self._format_uri(self.REVIEWS_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='reviews')

    def ratings(self, **kwargs):
        data = format_request_data(**kwargs)
        uri = self._format_uri(self.RATINGS_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='ratings')

    def ranks(self, start_date, end_date, **kwargs):
        data = self._format_data(start_date, end_date, **kwargs)
        uri = self._format_uri(self.RANKS_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='product_ranks')

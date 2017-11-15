from appannie.util import format_request_data


class Product(object):
    PRODUCTS_ENDPOINT = '/accounts/{account_id}/products'
    IAPS_ENDPOINT = '/accounts/{account_id}/products/{product_id}/iaps'
    SALES_ENDPOINT = '/accounts/{account_id}/products/{product_id}/sales'
    USAGE_ENDPOINT = '/accounts/{account_id}/products/{product_id}/{data_source}/usage'
    METRICS_ENDPOINT = '/accounts/{account_id}/products/{product_id}/store_metrics'

    def __init__(self, http_client, paginator, account_id, product_id=None):
        self.http_client = http_client
        self.paginator = paginator
        self.account_id = account_id
        self.product_id = product_id

    def _format_account_uri(self, uri):
        return uri.format(account_id=self.account_id)

    def _format_product_uri(self, uri, data_source=None):
        if not self.product_id:
            raise ValueError("Product id not specified")
        return uri.format(account_id=self.account_id,
                          product_id=self.product_id,
                          data_source=data_source or u'')

    def page(self, page=1):
        uri = self._format_account_uri(self.PRODUCTS_ENDPOINT)
        return self.paginator.make(uri).page(page)

    def all(self):
        uri = self._format_account_uri(self.PRODUCTS_ENDPOINT)
        return self.paginator.make(uri, union_key='products').all()

    def iaps(self):
        uri = self._format_product_uri(self.IAPS_ENDPOINT)
        return self.paginator.make(uri, union_key='iaps')

    def sales(self, union_key='sales_list', **kwargs):
        uri = self._format_product_uri(self.SALES_ENDPOINT)
        data = format_request_data(**kwargs)
        return self.paginator.make(uri, data=data, union_key=union_key)

    def usage(self, start_date, end_date, data_source='itc', **kwargs):
        data = format_request_data(start_date=start_date, end_date=end_date,
                                   **kwargs)
        uri = self._format_product_uri(self.USAGE_ENDPOINT,
                                       data_source=data_source)
        return self.paginator.make(uri, data=data, union_key='usage_list')

    def metrics(self, **kwargs):
        data = format_request_data(**kwargs)
        uri = self._format_product_uri(self.METRICS_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='metrics_list')

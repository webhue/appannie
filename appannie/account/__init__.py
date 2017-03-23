from appannie.util import format_request_data
from .product import Product


class Account(object):
    AD_SALES_ENDPOINT = '/ads/sales'
    SHARINGS_ENDPOINT = '/sharing/products'
    CONNECTIONS_ENDPOINT = '/accounts'
    ADS_ENDPOINT = '/accounts/{account_id}/ad_items'
    SALES_ENDPOINT = '/accounts/{account_id}/sales'

    def __init__(self, http_client, paginator, account_id):
        self.http_client = http_client
        self.paginator = paginator
        self.account_id = account_id

    def all(self):
        return self.paginator.make(self.CONNECTIONS_ENDPOINT,
                                   union_key='accounts').all()

    def page(self, page_number):
        return self.paginator.make(self.CONNECTIONS_ENDPOINT,
                                   union_key='accounts').page(page_number)

    def sharings(self):
        return self.paginator.make(self.SHARINGS_ENDPOINT,
                                   union_key='sharings')

    def ad_sales(self, **kwargs):
        if not kwargs.get('break_down'):
            raise ValueError("Break_down parameter is requireds")
        data = format_request_data(**kwargs)
        return self.paginator.make(self.AD_SALES_ENDPOINT,
                                   data=data,
                                   union_key='sales_list')

    def _validate_account_id(self):
        if not self.account_id:
            raise ValueError("Account id not specified")

    def _format_uri(self, uri):
        self._validate_account_id()
        return uri.format(account_id=self.account_id)

    def ads(self, **kwargs):
        uri = self._format_uri(self.ADS_ENDPOINT)
        data = format_request_data(**kwargs)
        return self.paginator.make(uri, data, 'ad_items')

    def sales(self, **kwargs):
        uri = self._format_uri(self.SALES_ENDPOINT)
        data = format_request_data(**kwargs)
        return self.paginator.make(uri, data, 'sales_list')

    def app(self, product_id=None):
        self._validate_account_id()
        return Product(self.http_client, self.paginator, self.account_id,
                       product_id)

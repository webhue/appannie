from .http import HttpClient
from .paginator import PaginatorFactory
from .metadata import Metadata
from .account import Account
from .store import Store
from .intelligence import Intelligence


class AppAnnie(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def http_client(self):
        return HttpClient(self.api_key)

    def paginator(self):
        return PaginatorFactory(self.http_client())

    def meta(self):
        return Metadata(self.http_client())

    def account(self, account_id=None):
        return Account(self.http_client(), self.paginator(), account_id)

    def store(self, market):
        return Store(self.http_client(), self.paginator(), market)

    def intelligence(self, market):
        return Intelligence(self.http_client(), self.paginator(), market)

class PaginatorFactory(object):
    def __init__(self, http_client):
        self.http_client = http_client

    def make(self, uri, data={}, union_key=None):
        return Paginator(self.http_client, uri, data, union_key)


class Paginator(object):
    def __init__(self, http_client, uri, data={}, union_key=None):
        self.http_client = http_client
        self.union_key = union_key
        self.uri = uri
        self.data = data

    def page(self, page=1):
        data = self.data.copy()
        data['page_index'] = page - 1

        return self.http_client.request(self.uri, data)

    def all(self):
        if not self.union_key:
            raise ValueError("Union key parameter is missing")

        union_result = []

        data = self.data.copy()

        page_num = 1
        page_index = 0

        while page_index < page_num:
            data['page_index'] = page_index
            page_result = self.http_client.request(self.uri, data)
            page_num = page_result.get('page_num')
            if page_num is None:
                break
            page_index = page_result.get('page_index') + 1
            page_result = page_result.get(self.union_key, [])
            union_result.extend(page_result)

        return union_result

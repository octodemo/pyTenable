from restfly.iterator import APIIterator


class Version1Iterator(APIIterator):
    '''
    This iterator conforms to the API v1 specification.
    '''
    _resource = None
    _path = None
    _query = dict()

    def _get_page(self):
        '''
        Collects the next page of resources
        '''
        # if the limit and offset weren't set, then we should set some defaults
        # to use here.
        self._query['offset'] = self._query.get('offset', 0)
        self._query['limit'] = self._query.get('limit', 1000)

        resp = self._api.get(self._path, params=self._query)
        self.page = resp[self._resource]
        self._query['offset'] += self._query['limit']
        self.total = resp.pagination.total


class Version2Iterator(APIIterator):
    '''
    This iterator conforms to the API v2 specification.
    '''
    _resource = None
    _path = None
    _query = dict()

    def _get_page(self):
        '''
        Collects the next page of resources
        '''
        # if the limit and offset weren't set, then we should set some defaults
        # to use here.
        self._query['page'] = self._query.get('page', 1)
        self._query['size'] = self._query.get('size', 1000)

        resp = self._api.get(self._path, params=self._query)
        self.page = resp['data'][self._resource]
        self._query['page'] += 1
        self.total = resp.total_count
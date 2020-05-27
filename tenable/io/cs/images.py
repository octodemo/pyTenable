from tenable.base.endpoint import APIEndpoint
from tenable.utils import dict_clean
from .iterator import ConSecIterator

class ImagesAPI(APIEndpoint):
    _path = 'container-security/api/v2/images'

    def list(self, **kwargs):
        kwargs['imageName'] = kwargs.get('image_name')
        kwargs['nameContains'] = kwargs.get('name_contains')
        return ConSecIterator(self._api,
            limit=kwargs.get('limit', 1000),
            offset=kwargs.get('offset', 0),
            _params=kwargs,
            _path='container-security/api/v2/repositories'
        )


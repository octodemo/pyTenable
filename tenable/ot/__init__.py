from tenable.platform import TenablePlatform
import os


class TenableOT(TenablePlatform):
    '''
    '''
    _base_path = '/v1'
    _env_base = 'TOT'
    _ssl_verify = False

    def _authenticate(self, **kwargs):
        '''
        Authentication method for Tenable.ot platform
        '''
        api_token = kwargs.get('api_token', os.getenv(
            '{}_API_TOKEN'.format(self._env_base)))

        self._session.headers.update({
            'Authorization': 'Key {token}'.format(token=api_token)
        })

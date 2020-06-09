from tenable.base.platform import APIPlatform
from restfly.errors import NotImplementedError
from .cs import ConSecAPI
from .lumin import LuminAPI
from .platform import PlatformAPI
from .vm import VulnMngtAPI
from .was import WebAppAPI
import json


def cloud_error_msg_func(r, **kwargs):
    '''
    Default message function for Cloud APIErrors

    Args:
        r (request.Response):
            The HTTP response that caused the error to be thrown.
        **kwargs (dict):
            The keyword argument dictionary from the APIError

    Returns:
        :obj:`str`:
            The string message for the error.
    '''
    return '[{code}: {verb}] {uri} request_uuid={uuid} body={body}'.format(
        code=str(r.status_code),
        verb=str(r.request.method),
        uri=str(r.request.url),
        uuid=str(r.headers.get('X-Request-Uuid')),
        body=str(r.content)
    )


class TenableIO(APIPlatform):
    '''
    '''
    _address = 'cloud.tenable.com'
    _env_base = 'TIO'

    def __init__(self, **kwargs):
        kwargs['error_func'] = kwargs.get('error_func', cloud_error_msg_func)
        super(TenableIO, self).__init__(**kwargs)

    def _resp_error_check(self, response, **kwargs):
        # no additional error checking is actually needed, however we want to
        # ensure that the request uuid is returned as a log message for every
        # response in the debug logs.
        self._log.debug('Response:{}'.format(json.dumps({
                'status': response.status_code,
                'method': response.request.method,
                'url': response.request.url,
                'request_uuid': response.headers.get('X-Request-Uuid'),
            })
        ))
        return response

    def _retry_request(self, resp, retries, **kwargs):
        '''
        The retry handler to provide additional context to the platform should
        a retry occur.
        '''
        h = kwargs.get('headers', dict())

        if resp.headers.get('X-Request-Uuid'):
            # If the Request UUID exists in the response, we will then send the
            # UUID of the current request along with the next request.  This
            # allows for tracking when requests were retried within the
            # platform.
            h['X-Tio-Last-Requested-Uuid'] = resp.headers.get('X-Request-Uuid')

        # We will also pass the retry count to the next request as well.
        h['X-Tio-Retry-Count'] = str(retries)

        kwargs['headers'] = h
        return kwargs

    @property
    def cs(self):
        '''
        The interface object for the
        :doc:`Tenable.io Container Security APIs <cs/index>`.
        '''
        #return ConSecAPI(self)
        raise NotImplementedError('ConSec API Interface not yet written.')

    @property
    def lumin(self):
        '''
        The interface object for the :doc:`Tenable.io Lumin APIs <lumin/index>`.
        '''
        #return LuminAPI(self)
        raise NotImplementedError('Lumin API Interface not yet written.')

    @property
    def platform(self):
        '''
        The interface object for the
        :doc:`Tenable.io Platform APIs <platform/index>`.
        '''
        return PlatformAPI(self)

    @property
    def vm(self):
        '''
        The interface object for the
        :doc:`Tenable.io Vulnerability Management APIs <vm/index>`.
        '''
        return VulnMngtAPI(self)
        #raise NotImplementedError('VM API Interface not yet written.')

    @property
    def was(self):
        '''
        The interface object for the
        :doc:`Tenable.io Web Application Scanning APIs <was/index>`.
        '''
        #return WebAppAPI(self)
        raise NotImplementedError('WAS API Interface not yet written.')

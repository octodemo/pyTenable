from tenable.base.platform import APIPlatform
from .cs import ConSecAPI
from .lumin import LuminAPI
from .platform import PlatformAPI
from .vm import VulnMngtAPI
from .was import WebAppAPI


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
        The interface object for Tenable.io Container Security.  See the
        :doc:`cs documentation <cs/index>` for full details.
        '''
        return ConSecAPI(self)

    @property
    def lumin(self):
        '''
        The interface object for Tenable.io Lumin.  See the
        :doc:`lumin documentation <lumin/index>` for full details.
        '''
        return LuminAPI(self)

    @property
    def platform(self):
        '''
        The interface object for Tenable.io platform.  See the
        :doc:`platform documentation <platform/index>` for full details.
        '''
        return PlatformAPI(self)

    @property
    def vm(self):
        '''
        The interface object for Tenable.io Vulnerability Management.  See the
        :doc:`vm documentation <vm/index>` for full details.
        '''
        return VulnMngtAPI(self)

    @property
    def was(self):
        '''
        The interface object for Tenable.io Web Application Scanning.  See the
        :doc:`was documentation <was/index>` for full details.
        '''
        return WebAppAPI(self)

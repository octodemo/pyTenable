from restfly import APISession
from tenable import __version__
import os


class APIPlatform(APISession):
    _lib_name = 'pyTenable'
    _lib_version = __version__
    _box = True
    _retries = 5
    _env_base = ''
    _base_path = ''
    _port = 443
    _scheme = 'https'
    _address = None
    _auth = (None, None)
    _auth_mech = None

    def __init__(self, **kwargs):
        # Constructing the URL from the various parameters.
        self._url = '{}://{}:{}{}'.format(
            kwargs.get('scheme', self._scheme),
            kwargs.get('address', os.getenv(
                '{}_ADDRESS'.format(self._env_base), self._address)),
            kwargs.get('port', os.getenv(
                '{}_PORT'.format(self._env_base), self._port)),
            kwargs.get('base_path', self._base_path)
        )
        super(APIPlatform, self).__init__(**kwargs)

    def _authenticate(self, **kwargs):
        '''
        This method handles authentication for both API Keys and for session
        authentication.
        '''

        # These functions determine how authentication is to be handled within
        # for both session authentication and key-based authentication.  They
        # have been broken down into these functions for easy overloading.
        def key_auth():
            '''
            Default API Key Auth Behavior
            '''
            self._session.headers.update({
                'X-APIKeys': 'accessKey={}; secretKey={}'.format(*keys)
            })
            self._auth_mech = 'keys'

        def s_auth():
            '''
            Default Session auth behavior
            '''
            self.post('session', json={
                'username': self._auth[0],
                'password': self._auth[1]
            })
            self._auth_mech = 'user'

        # Here we are grafting the authentication functions into the keyword
        # arguments for later usage.  If a function is provided in the keywords
        # under the key names below, we will use those instead.  This should
        # essentially allow for the authentication logic to be overridden with
        # minimal effort.
        kwargs['key_auth_func'] = kwargs.get('key_auth_func', key_auth)
        kwargs['session_auth_func'] = kwargs.get('session_auth_func', s_auth)

        # Pull the API keys from the keyword arguments passed to the constructor
        # and build the keys tuple.  As API Keys will be injected directly into
        # the session, there is no need to store these.
        keys = (
            kwargs.get('access_key', os.getenv(
                '{}_ACCESS_KEY'.format(self._env_base))),
            kwargs.get('secret_key', os.getenv(
                '{}_SECRET_KEY'.format(self._env_base)))
        )

        # The session authentication tuple.  We will be storing these as its
        # possible for the session to timeout on the user.  This would require
        # re-authentication.
        self._auth = (
            kwargs.get('username', os.getenv(
                '{}_USERNAME'.format(self._env_base))),
            kwargs.get('password', os.getenv(
                '{}_PASSWORD'.format(self._env_base)))
        )

        # Run the desired authentication function.  As API keys are generally
        # preferred over session authentication, we will first check to see that
        # keys have been
        if None not in keys:
            kwargs['key_auth_func']()
        elif None not in self._auth:
            kwargs['session_auth_func']()
        else:
            self._log.warning('Starting an unauthenticated session.')

    def _deauthenticate(self):
        '''
        This method handles de-authentication.  This is only necessary for
        session-based authentication.
        '''
        if self._auth_mech == 'user':
            self.delete('session')
        self._auth = (None, None)
        self._auth_mech = None
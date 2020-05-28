from tenable.base.endpoint import APIEndpoint
from restfly.iterator import APIIterator


from .connectors import ConnectorsAPI
from .groups import GroupsAPI
from .session import SessionAPI
from .users import UsersAPI


class PlatformAPI(APIEndpoint):
    '''
    '''
    @property
    def connectors(self):
        '''
        The interface object for connectors API  See the
        :doc:`connectors documentation <connectors>` for full details.
        '''
        #return ConnectorsAPI(self._api)

    @property
    def groups(self):
        '''
        The interface object for user groups API  See the
        :doc:`groups documentation <groups>` for full details.
        '''
        return GroupsAPI(self._api)

    @property
    def session(self):
        '''
        The interface object for session API  See the
        :doc:`session documentation <session>` for full details.
        '''
        return SessionAPI(self._api)

    @property
    def users(self):
        '''
        The interface object for users API  See the
        :doc:`users documentation <users>` for full details.
        '''
        return UsersAPI(self._api)
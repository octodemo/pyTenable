'''
'''
from tenable.base.endpoint import APIEndpoint
from restfly.iterator import APIIterator


#from .connectors import ConnectorsAPI
#from .groups import GroupsAPI
from .session import SessionAPI
from .users import UsersAPI


class PlatformAPI(APIEndpoint):
    '''
    '''
#    @property
#    def connectors(self):
#        '''
#        '''
#        return ConnectorsAPI(self._api)

#    @property
#    def groups(self):
#        '''
#        '''
#        return GroupsAPI(self._api)

    @property
    def session(self):
        '''
        '''
        return SessionAPI(self._api)

    @property
    def users(self):
        '''
        '''
        return UsersAPI(self._api)
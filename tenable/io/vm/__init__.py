from tenable.base.endpoint import APIEndpoint
from .access_groups import AccessGroupsAPI
from .filters import FiltersAPI

class VulnMngtAPI(APIEndpoint):
    @property
    def access_groups(self):
        '''
        The interface object for the :doc:`Access Groups APIs <access_groups>`.
        '''
        return AccessGroupsAPI(self._api)

    @property
    def filters(self):
        '''
        The interface object for the :doc:`Filters APIs <filters>`.
        '''
        return FiltersAPI(self._api)
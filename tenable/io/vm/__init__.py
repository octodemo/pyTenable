'''
Vuln Management
===============

.. toctree::
    :hidden:
    :glob:

    access_groups
    agent_config
    agent_exclusions
    agents
    exclusions
    filters

.. rst-class:: hide-signature
.. autoclass:: VulnMngtAPI
    :members:
'''
from tenable.base.endpoint import APIEndpoint

from .access_groups import AccessGroupsAPI
from .agent_config import AgentConfigAPI
from .agent_exclusions import AgentExclusionsAPI
from .agents import AgentsAPI
from .assets import AssetsAPI
from .exclusions import ExclusionsAPI
from .filters import FiltersAPI

class VulnMngtAPI(APIEndpoint):
    @property
    def access_groups(self):
        '''
        The interface object for the :doc:`Access Groups APIs <access_groups>`.
        '''
        return AccessGroupsAPI(self._api)

    @property
    def agent_config(self):
        '''
        The interface object for the :doc:`Agent Config APIs <agent_config>`.
        '''
        return AgentConfigAPI(self._api)

    @property
    def agent_exclusions(self):
        '''
        The interface object for the :doc:`Agent Exclusion APIs <agent_exclusions>`.
        '''
        return AgentExclusionsAPI(self._api)

    @property
    def agents(self):
        '''
        The interface object for the :doc:`Agents APIs <agents>`.
        '''
        return AgentsAPI(self._api)

    @property
    def assets(self):
        '''
        The interface object for the :doc:`Assets APIs <assets>`.
        '''
        return AssetsAPI(self._api)

    @property
    def exclusions(self):
        '''
        The interface object for the :doc:`Exclusions APIs <exclusions>`.
        '''
        return ExclusionsAPI(self._api)

    @property
    def filters(self):
        '''
        The interface object for the :doc:`Filters APIs <filters>`.
        '''
        return FiltersAPI(self._api)
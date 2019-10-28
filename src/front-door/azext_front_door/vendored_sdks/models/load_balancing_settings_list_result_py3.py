# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LoadBalancingSettingsListResult(Model):
    """Result of the request to list load balancing settings. It contains a list
    of load balancing settings objects and a URL link to get the next set of
    results.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: List of Backend Pools within a Front Door.
    :vartype value:
     list[~azure.mgmt.frontdoor.models.LoadBalancingSettingsModel]
    :param next_link: URL to get the next set of LoadBalancingSettings objects
     if there are any.
    :type next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[LoadBalancingSettingsModel]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, next_link: str=None, **kwargs) -> None:
        super(LoadBalancingSettingsListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = next_link
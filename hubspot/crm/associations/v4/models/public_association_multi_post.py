# coding: utf-8

"""
    CrmPublicAssociationsServiceV4

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.associations.v4.configuration import Configuration


class PublicAssociationMultiPost(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"_from": "PublicObjectId", "to": "PublicObjectId", "types": "list[AssociationSpec]"}

    attribute_map = {"_from": "from", "to": "to", "types": "types"}

    def __init__(self, _from=None, to=None, types=None, local_vars_configuration=None):  # noqa: E501
        """PublicAssociationMultiPost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._to = None
        self._types = None
        self.discriminator = None

        self._from = _from
        self.to = to
        self.types = types

    @property
    def _from(self):
        """Gets the _from of this PublicAssociationMultiPost.  # noqa: E501


        :return: The _from of this PublicAssociationMultiPost.  # noqa: E501
        :rtype: PublicObjectId
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this PublicAssociationMultiPost.


        :param _from: The _from of this PublicAssociationMultiPost.  # noqa: E501
        :type: PublicObjectId
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this PublicAssociationMultiPost.  # noqa: E501


        :return: The to of this PublicAssociationMultiPost.  # noqa: E501
        :rtype: PublicObjectId
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PublicAssociationMultiPost.


        :param to: The to of this PublicAssociationMultiPost.  # noqa: E501
        :type: PublicObjectId
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def types(self):
        """Gets the types of this PublicAssociationMultiPost.  # noqa: E501


        :return: The types of this PublicAssociationMultiPost.  # noqa: E501
        :rtype: list[AssociationSpec]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this PublicAssociationMultiPost.


        :param types: The types of this PublicAssociationMultiPost.  # noqa: E501
        :type: list[AssociationSpec]
        """
        if self.local_vars_configuration.client_side_validation and types is None:  # noqa: E501
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501

        self._types = types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicAssociationMultiPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAssociationMultiPost):
            return True

        return self.to_dict() != other.to_dict()

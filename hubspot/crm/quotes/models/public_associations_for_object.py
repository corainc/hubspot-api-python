# coding: utf-8

"""
    Quotes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.quotes.configuration import Configuration


class PublicAssociationsForObject(object):
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
    openapi_types = {"types": "list[AssociationSpec]", "to": "PublicObjectId"}

    attribute_map = {"types": "types", "to": "to"}

    def __init__(self, types=None, to=None, local_vars_configuration=None):  # noqa: E501
        """PublicAssociationsForObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._types = None
        self._to = None
        self.discriminator = None

        self.types = types
        self.to = to

    @property
    def types(self):
        """Gets the types of this PublicAssociationsForObject.  # noqa: E501


        :return: The types of this PublicAssociationsForObject.  # noqa: E501
        :rtype: list[AssociationSpec]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this PublicAssociationsForObject.


        :param types: The types of this PublicAssociationsForObject.  # noqa: E501
        :type types: list[AssociationSpec]
        """
        if self.local_vars_configuration.client_side_validation and types is None:  # noqa: E501
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501

        self._types = types

    @property
    def to(self):
        """Gets the to of this PublicAssociationsForObject.  # noqa: E501


        :return: The to of this PublicAssociationsForObject.  # noqa: E501
        :rtype: PublicObjectId
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PublicAssociationsForObject.


        :param to: The to of this PublicAssociationsForObject.  # noqa: E501
        :type to: PublicObjectId
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicAssociationsForObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAssociationsForObject):
            return True

        return self.to_dict() != other.to_dict()

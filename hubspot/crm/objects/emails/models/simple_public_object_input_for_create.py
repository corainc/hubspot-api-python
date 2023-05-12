# coding: utf-8

"""
    Emails

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

from hubspot.crm.objects.emails.configuration import Configuration


class SimplePublicObjectInputForCreate(object):
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
    openapi_types = {"properties": "dict[str, str]", "associations": "list[PublicAssociationsForObject]"}

    attribute_map = {"properties": "properties", "associations": "associations"}

    def __init__(self, properties=None, associations=None, local_vars_configuration=None):  # noqa: E501
        """SimplePublicObjectInputForCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._properties = None
        self._associations = None
        self.discriminator = None

        self.properties = properties
        self.associations = associations

    @property
    def properties(self):
        """Gets the properties of this SimplePublicObjectInputForCreate.  # noqa: E501


        :return: The properties of this SimplePublicObjectInputForCreate.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SimplePublicObjectInputForCreate.


        :param properties: The properties of this SimplePublicObjectInputForCreate.  # noqa: E501
        :type properties: dict[str, str]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def associations(self):
        """Gets the associations of this SimplePublicObjectInputForCreate.  # noqa: E501


        :return: The associations of this SimplePublicObjectInputForCreate.  # noqa: E501
        :rtype: list[PublicAssociationsForObject]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this SimplePublicObjectInputForCreate.


        :param associations: The associations of this SimplePublicObjectInputForCreate.  # noqa: E501
        :type associations: list[PublicAssociationsForObject]
        """
        if self.local_vars_configuration.client_side_validation and associations is None:  # noqa: E501
            raise ValueError("Invalid value for `associations`, must not be `None`")  # noqa: E501

        self._associations = associations

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
        if not isinstance(other, SimplePublicObjectInputForCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimplePublicObjectInputForCreate):
            return True

        return self.to_dict() != other.to_dict()
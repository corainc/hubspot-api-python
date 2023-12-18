# coding: utf-8

"""
    Lists

    CRUD operations to manage lists and list memberships  # noqa: E501

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

from hubspot.crm.lists.configuration import Configuration


class PublicTimeOffset(object):
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
    openapi_types = {"offset_direction": "str", "time_unit": "str", "amount": "int"}

    attribute_map = {"offset_direction": "offsetDirection", "time_unit": "timeUnit", "amount": "amount"}

    def __init__(self, offset_direction=None, time_unit=None, amount=None, local_vars_configuration=None):  # noqa: E501
        """PublicTimeOffset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._offset_direction = None
        self._time_unit = None
        self._amount = None
        self.discriminator = None

        self.offset_direction = offset_direction
        self.time_unit = time_unit
        self.amount = amount

    @property
    def offset_direction(self):
        """Gets the offset_direction of this PublicTimeOffset.  # noqa: E501


        :return: The offset_direction of this PublicTimeOffset.  # noqa: E501
        :rtype: str
        """
        return self._offset_direction

    @offset_direction.setter
    def offset_direction(self, offset_direction):
        """Sets the offset_direction of this PublicTimeOffset.


        :param offset_direction: The offset_direction of this PublicTimeOffset.  # noqa: E501
        :type offset_direction: str
        """
        if self.local_vars_configuration.client_side_validation and offset_direction is None:  # noqa: E501
            raise ValueError("Invalid value for `offset_direction`, must not be `None`")  # noqa: E501

        self._offset_direction = offset_direction

    @property
    def time_unit(self):
        """Gets the time_unit of this PublicTimeOffset.  # noqa: E501


        :return: The time_unit of this PublicTimeOffset.  # noqa: E501
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this PublicTimeOffset.


        :param time_unit: The time_unit of this PublicTimeOffset.  # noqa: E501
        :type time_unit: str
        """
        if self.local_vars_configuration.client_side_validation and time_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `time_unit`, must not be `None`")  # noqa: E501

        self._time_unit = time_unit

    @property
    def amount(self):
        """Gets the amount of this PublicTimeOffset.  # noqa: E501


        :return: The amount of this PublicTimeOffset.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PublicTimeOffset.


        :param amount: The amount of this PublicTimeOffset.  # noqa: E501
        :type amount: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if not isinstance(other, PublicTimeOffset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicTimeOffset):
            return True

        return self.to_dict() != other.to_dict()

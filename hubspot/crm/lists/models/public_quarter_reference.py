# coding: utf-8

"""
    Lists

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

from hubspot.crm.lists.configuration import Configuration


class PublicQuarterReference(object):
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
    openapi_types = {"hour": "int", "month": "int", "millisecond": "int", "reference_type": "str", "day": "int", "minute": "int", "second": "int"}

    attribute_map = {"hour": "hour", "month": "month", "millisecond": "millisecond", "reference_type": "referenceType", "day": "day", "minute": "minute", "second": "second"}

    def __init__(self, hour=None, month=None, millisecond=None, reference_type="QUARTER", day=None, minute=None, second=None, local_vars_configuration=None):  # noqa: E501
        """PublicQuarterReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hour = None
        self._month = None
        self._millisecond = None
        self._reference_type = None
        self._day = None
        self._minute = None
        self._second = None
        self.discriminator = None

        if hour is not None:
            self.hour = hour
        self.month = month
        if millisecond is not None:
            self.millisecond = millisecond
        self.reference_type = reference_type
        self.day = day
        if minute is not None:
            self.minute = minute
        if second is not None:
            self.second = second

    @property
    def hour(self):
        """Gets the hour of this PublicQuarterReference.  # noqa: E501


        :return: The hour of this PublicQuarterReference.  # noqa: E501
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this PublicQuarterReference.


        :param hour: The hour of this PublicQuarterReference.  # noqa: E501
        :type hour: int
        """

        self._hour = hour

    @property
    def month(self):
        """Gets the month of this PublicQuarterReference.  # noqa: E501


        :return: The month of this PublicQuarterReference.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this PublicQuarterReference.


        :param month: The month of this PublicQuarterReference.  # noqa: E501
        :type month: int
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def millisecond(self):
        """Gets the millisecond of this PublicQuarterReference.  # noqa: E501


        :return: The millisecond of this PublicQuarterReference.  # noqa: E501
        :rtype: int
        """
        return self._millisecond

    @millisecond.setter
    def millisecond(self, millisecond):
        """Sets the millisecond of this PublicQuarterReference.


        :param millisecond: The millisecond of this PublicQuarterReference.  # noqa: E501
        :type millisecond: int
        """

        self._millisecond = millisecond

    @property
    def reference_type(self):
        """Gets the reference_type of this PublicQuarterReference.  # noqa: E501


        :return: The reference_type of this PublicQuarterReference.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this PublicQuarterReference.


        :param reference_type: The reference_type of this PublicQuarterReference.  # noqa: E501
        :type reference_type: str
        """
        if self.local_vars_configuration.client_side_validation and reference_type is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QUARTER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reference_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `reference_type` ({0}), must be one of {1}".format(reference_type, allowed_values))  # noqa: E501

        self._reference_type = reference_type

    @property
    def day(self):
        """Gets the day of this PublicQuarterReference.  # noqa: E501


        :return: The day of this PublicQuarterReference.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this PublicQuarterReference.


        :param day: The day of this PublicQuarterReference.  # noqa: E501
        :type day: int
        """
        if self.local_vars_configuration.client_side_validation and day is None:  # noqa: E501
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def minute(self):
        """Gets the minute of this PublicQuarterReference.  # noqa: E501


        :return: The minute of this PublicQuarterReference.  # noqa: E501
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this PublicQuarterReference.


        :param minute: The minute of this PublicQuarterReference.  # noqa: E501
        :type minute: int
        """

        self._minute = minute

    @property
    def second(self):
        """Gets the second of this PublicQuarterReference.  # noqa: E501


        :return: The second of this PublicQuarterReference.  # noqa: E501
        :rtype: int
        """
        return self._second

    @second.setter
    def second(self, second):
        """Sets the second of this PublicQuarterReference.


        :param second: The second of this PublicQuarterReference.  # noqa: E501
        :type second: int
        """

        self._second = second

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
        if not isinstance(other, PublicQuarterReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicQuarterReference):
            return True

        return self.to_dict() != other.to_dict()

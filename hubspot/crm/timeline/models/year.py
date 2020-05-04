# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM object like contacts, companies, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.timeline.configuration import Configuration


class Year(object):
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
    openapi_types = {
        "operator": "str",
        "value": "float",
        "inputs": "list[AnyOfConstantBooleanConstantNumberConstantStringBooleanPropertyVariableStringPropertyVariableNumberPropertyVariableAddNumbersSubtractNumbersMultiplyNumbersDivideNumbersRoundDownNumbersRoundUpNumbersUpperCaseLowerCaseConcatStringsContainsBeginsWithNumberToStringParseNumberFetchExchangeRatePipelineProbabilityMaxNumbersMinNumbersLessThanLessThanOrEqualMoreThanMoreThanOrEqualNumberEqualsStringEqualsNotDateMonthYearNowTimeBetweenPeriodToMonthsAndOrXorIfStringIfNumberIfBooleanIsPresentHasEmailReplyHasPlainTextEmailReplyExtractMostRecentEmailReplyHtmlExtractMostRecentEmailReplyTextExtractMostRecentPlainTextEmailReply]",
        "property_name": "str",
    }

    attribute_map = {
        "operator": "operator",
        "value": "value",
        "inputs": "inputs",
        "property_name": "propertyName",
    }

    def __init__(
        self,
        operator="YEAR",
        value=None,
        inputs=None,
        property_name=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Year - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._operator = None
        self._value = None
        self._inputs = None
        self._property_name = None
        self.discriminator = None

        self.operator = operator
        if value is not None:
            self.value = value
        if inputs is not None:
            self.inputs = inputs
        if property_name is not None:
            self.property_name = property_name

    @property
    def operator(self):
        """Gets the operator of this Year.  # noqa: E501


        :return: The operator of this Year.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Year.


        :param operator: The operator of this Year.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and operator is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `operator`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["YEAR"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and operator not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}".format(  # noqa: E501
                    operator, allowed_values
                )
            )

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this Year.  # noqa: E501


        :return: The value of this Year.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Year.


        :param value: The value of this Year.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def inputs(self):
        """Gets the inputs of this Year.  # noqa: E501


        :return: The inputs of this Year.  # noqa: E501
        :rtype: list[AnyOfConstantBooleanConstantNumberConstantStringBooleanPropertyVariableStringPropertyVariableNumberPropertyVariableAddNumbersSubtractNumbersMultiplyNumbersDivideNumbersRoundDownNumbersRoundUpNumbersUpperCaseLowerCaseConcatStringsContainsBeginsWithNumberToStringParseNumberFetchExchangeRatePipelineProbabilityMaxNumbersMinNumbersLessThanLessThanOrEqualMoreThanMoreThanOrEqualNumberEqualsStringEqualsNotDateMonthYearNowTimeBetweenPeriodToMonthsAndOrXorIfStringIfNumberIfBooleanIsPresentHasEmailReplyHasPlainTextEmailReplyExtractMostRecentEmailReplyHtmlExtractMostRecentEmailReplyTextExtractMostRecentPlainTextEmailReply]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Year.


        :param inputs: The inputs of this Year.  # noqa: E501
        :type: list[AnyOfConstantBooleanConstantNumberConstantStringBooleanPropertyVariableStringPropertyVariableNumberPropertyVariableAddNumbersSubtractNumbersMultiplyNumbersDivideNumbersRoundDownNumbersRoundUpNumbersUpperCaseLowerCaseConcatStringsContainsBeginsWithNumberToStringParseNumberFetchExchangeRatePipelineProbabilityMaxNumbersMinNumbersLessThanLessThanOrEqualMoreThanMoreThanOrEqualNumberEqualsStringEqualsNotDateMonthYearNowTimeBetweenPeriodToMonthsAndOrXorIfStringIfNumberIfBooleanIsPresentHasEmailReplyHasPlainTextEmailReplyExtractMostRecentEmailReplyHtmlExtractMostRecentEmailReplyTextExtractMostRecentPlainTextEmailReply]
        """

        self._inputs = inputs

    @property
    def property_name(self):
        """Gets the property_name of this Year.  # noqa: E501


        :return: The property_name of this Year.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this Year.


        :param property_name: The property_name of this Year.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, Year):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Year):
            return True

        return self.to_dict() != other.to_dict()

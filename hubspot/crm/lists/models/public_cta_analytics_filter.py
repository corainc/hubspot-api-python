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


class PublicCtaAnalyticsFilter(object):
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
        "filter_type": "str",
        "coalescing_refine_by": "PublicEventAnalyticsFilterCoalescingRefineBy",
        "pruning_refine_by": "PublicEventAnalyticsFilterCoalescingRefineBy",
        "operator": "str",
        "cta_name": "str",
    }

    attribute_map = {"filter_type": "filterType", "coalescing_refine_by": "coalescingRefineBy", "pruning_refine_by": "pruningRefineBy", "operator": "operator", "cta_name": "ctaName"}

    def __init__(self, filter_type="CTA", coalescing_refine_by=None, pruning_refine_by=None, operator=None, cta_name=None, local_vars_configuration=None):  # noqa: E501
        """PublicCtaAnalyticsFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_type = None
        self._coalescing_refine_by = None
        self._pruning_refine_by = None
        self._operator = None
        self._cta_name = None
        self.discriminator = None

        self.filter_type = filter_type
        if coalescing_refine_by is not None:
            self.coalescing_refine_by = coalescing_refine_by
        if pruning_refine_by is not None:
            self.pruning_refine_by = pruning_refine_by
        self.operator = operator
        self.cta_name = cta_name

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicCtaAnalyticsFilter.  # noqa: E501


        :return: The filter_type of this PublicCtaAnalyticsFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicCtaAnalyticsFilter.


        :param filter_type: The filter_type of this PublicCtaAnalyticsFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CTA"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def coalescing_refine_by(self):
        """Gets the coalescing_refine_by of this PublicCtaAnalyticsFilter.  # noqa: E501


        :return: The coalescing_refine_by of this PublicCtaAnalyticsFilter.  # noqa: E501
        :rtype: PublicEventAnalyticsFilterCoalescingRefineBy
        """
        return self._coalescing_refine_by

    @coalescing_refine_by.setter
    def coalescing_refine_by(self, coalescing_refine_by):
        """Sets the coalescing_refine_by of this PublicCtaAnalyticsFilter.


        :param coalescing_refine_by: The coalescing_refine_by of this PublicCtaAnalyticsFilter.  # noqa: E501
        :type coalescing_refine_by: PublicEventAnalyticsFilterCoalescingRefineBy
        """

        self._coalescing_refine_by = coalescing_refine_by

    @property
    def pruning_refine_by(self):
        """Gets the pruning_refine_by of this PublicCtaAnalyticsFilter.  # noqa: E501


        :return: The pruning_refine_by of this PublicCtaAnalyticsFilter.  # noqa: E501
        :rtype: PublicEventAnalyticsFilterCoalescingRefineBy
        """
        return self._pruning_refine_by

    @pruning_refine_by.setter
    def pruning_refine_by(self, pruning_refine_by):
        """Sets the pruning_refine_by of this PublicCtaAnalyticsFilter.


        :param pruning_refine_by: The pruning_refine_by of this PublicCtaAnalyticsFilter.  # noqa: E501
        :type pruning_refine_by: PublicEventAnalyticsFilterCoalescingRefineBy
        """

        self._pruning_refine_by = pruning_refine_by

    @property
    def operator(self):
        """Gets the operator of this PublicCtaAnalyticsFilter.  # noqa: E501


        :return: The operator of this PublicCtaAnalyticsFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicCtaAnalyticsFilter.


        :param operator: The operator of this PublicCtaAnalyticsFilter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def cta_name(self):
        """Gets the cta_name of this PublicCtaAnalyticsFilter.  # noqa: E501


        :return: The cta_name of this PublicCtaAnalyticsFilter.  # noqa: E501
        :rtype: str
        """
        return self._cta_name

    @cta_name.setter
    def cta_name(self, cta_name):
        """Sets the cta_name of this PublicCtaAnalyticsFilter.


        :param cta_name: The cta_name of this PublicCtaAnalyticsFilter.  # noqa: E501
        :type cta_name: str
        """
        if self.local_vars_configuration.client_side_validation and cta_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cta_name`, must not be `None`")  # noqa: E501

        self._cta_name = cta_name

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
        if not isinstance(other, PublicCtaAnalyticsFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicCtaAnalyticsFilter):
            return True

        return self.to_dict() != other.to_dict()

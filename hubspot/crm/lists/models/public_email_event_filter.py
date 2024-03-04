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


class PublicEmailEventFilter(object):
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
        "click_url": "str",
        "level": "str",
        "pruning_refine_by": "PublicEventAnalyticsFilterCoalescingRefineBy",
        "app_id": "str",
        "email_id": "str",
        "filter_type": "str",
        "operator": "str",
    }

    attribute_map = {"click_url": "clickUrl", "level": "level", "pruning_refine_by": "pruningRefineBy", "app_id": "appId", "email_id": "emailId", "filter_type": "filterType", "operator": "operator"}

    def __init__(self, click_url=None, level=None, pruning_refine_by=None, app_id=None, email_id=None, filter_type="EMAIL_EVENT", operator=None, local_vars_configuration=None):  # noqa: E501
        """PublicEmailEventFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._click_url = None
        self._level = None
        self._pruning_refine_by = None
        self._app_id = None
        self._email_id = None
        self._filter_type = None
        self._operator = None
        self.discriminator = None

        if click_url is not None:
            self.click_url = click_url
        self.level = level
        if pruning_refine_by is not None:
            self.pruning_refine_by = pruning_refine_by
        self.app_id = app_id
        self.email_id = email_id
        self.filter_type = filter_type
        self.operator = operator

    @property
    def click_url(self):
        """Gets the click_url of this PublicEmailEventFilter.  # noqa: E501


        :return: The click_url of this PublicEmailEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._click_url

    @click_url.setter
    def click_url(self, click_url):
        """Sets the click_url of this PublicEmailEventFilter.


        :param click_url: The click_url of this PublicEmailEventFilter.  # noqa: E501
        :type click_url: str
        """

        self._click_url = click_url

    @property
    def level(self):
        """Gets the level of this PublicEmailEventFilter.  # noqa: E501


        :return: The level of this PublicEmailEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this PublicEmailEventFilter.


        :param level: The level of this PublicEmailEventFilter.  # noqa: E501
        :type level: str
        """
        if self.local_vars_configuration.client_side_validation and level is None:  # noqa: E501
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def pruning_refine_by(self):
        """Gets the pruning_refine_by of this PublicEmailEventFilter.  # noqa: E501


        :return: The pruning_refine_by of this PublicEmailEventFilter.  # noqa: E501
        :rtype: PublicEventAnalyticsFilterCoalescingRefineBy
        """
        return self._pruning_refine_by

    @pruning_refine_by.setter
    def pruning_refine_by(self, pruning_refine_by):
        """Sets the pruning_refine_by of this PublicEmailEventFilter.


        :param pruning_refine_by: The pruning_refine_by of this PublicEmailEventFilter.  # noqa: E501
        :type pruning_refine_by: PublicEventAnalyticsFilterCoalescingRefineBy
        """

        self._pruning_refine_by = pruning_refine_by

    @property
    def app_id(self):
        """Gets the app_id of this PublicEmailEventFilter.  # noqa: E501


        :return: The app_id of this PublicEmailEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this PublicEmailEventFilter.


        :param app_id: The app_id of this PublicEmailEventFilter.  # noqa: E501
        :type app_id: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def email_id(self):
        """Gets the email_id of this PublicEmailEventFilter.  # noqa: E501


        :return: The email_id of this PublicEmailEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this PublicEmailEventFilter.


        :param email_id: The email_id of this PublicEmailEventFilter.  # noqa: E501
        :type email_id: str
        """
        if self.local_vars_configuration.client_side_validation and email_id is None:  # noqa: E501
            raise ValueError("Invalid value for `email_id`, must not be `None`")  # noqa: E501

        self._email_id = email_id

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicEmailEventFilter.  # noqa: E501


        :return: The filter_type of this PublicEmailEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicEmailEventFilter.


        :param filter_type: The filter_type of this PublicEmailEventFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["EMAIL_EVENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def operator(self):
        """Gets the operator of this PublicEmailEventFilter.  # noqa: E501


        :return: The operator of this PublicEmailEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicEmailEventFilter.


        :param operator: The operator of this PublicEmailEventFilter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = [
            "LINK_CLICKED",
            "MARKED_SPAM",
            "OPENED",
            "OPENED_BUT_LINK_NOT_CLICKED",
            "OPENED_BUT_NOT_REPLIED",
            "REPLIED",
            "UNSUBSCRIBED",
            "BOUNCED",
            "RECEIVED",
            "RECEIVED_BUT_NOT_OPENED",
            "SENT",
            "SENT_BUT_LINK_NOT_CLICKED",
            "SENT_BUT_NOT_RECEIVED",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operator not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `operator` ({0}), must be one of {1}".format(operator, allowed_values))  # noqa: E501

        self._operator = operator

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
        if not isinstance(other, PublicEmailEventFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicEmailEventFilter):
            return True

        return self.to_dict() != other.to_dict()

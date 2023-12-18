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


class PublicObjectList(object):
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
        "processing_type": "str",
        "object_type_id": "str",
        "updated_by_id": "int",
        "filters_updated_at": "datetime",
        "list_id": "int",
        "created_at": "datetime",
        "processing_status": "str",
        "deleted_at": "datetime",
        "list_version": "int",
        "name": "str",
        "created_by_id": "int",
        "filter_branch": "PublicPropertyAssociationFilterBranchFilterBranchesInner",
        "updated_at": "datetime",
    }

    attribute_map = {
        "processing_type": "processingType",
        "object_type_id": "objectTypeId",
        "updated_by_id": "updatedById",
        "filters_updated_at": "filtersUpdatedAt",
        "list_id": "listId",
        "created_at": "createdAt",
        "processing_status": "processingStatus",
        "deleted_at": "deletedAt",
        "list_version": "listVersion",
        "name": "name",
        "created_by_id": "createdById",
        "filter_branch": "filterBranch",
        "updated_at": "updatedAt",
    }

    def __init__(
        self,
        processing_type=None,
        object_type_id=None,
        updated_by_id=None,
        filters_updated_at=None,
        list_id=None,
        created_at=None,
        processing_status=None,
        deleted_at=None,
        list_version=None,
        name=None,
        created_by_id=None,
        filter_branch=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicObjectList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._processing_type = None
        self._object_type_id = None
        self._updated_by_id = None
        self._filters_updated_at = None
        self._list_id = None
        self._created_at = None
        self._processing_status = None
        self._deleted_at = None
        self._list_version = None
        self._name = None
        self._created_by_id = None
        self._filter_branch = None
        self._updated_at = None
        self.discriminator = None

        self.processing_type = processing_type
        self.object_type_id = object_type_id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if filters_updated_at is not None:
            self.filters_updated_at = filters_updated_at
        self.list_id = list_id
        if created_at is not None:
            self.created_at = created_at
        self.processing_status = processing_status
        if deleted_at is not None:
            self.deleted_at = deleted_at
        self.list_version = list_version
        self.name = name
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if filter_branch is not None:
            self.filter_branch = filter_branch
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def processing_type(self):
        """Gets the processing_type of this PublicObjectList.  # noqa: E501

        The processing type of the list.  # noqa: E501

        :return: The processing_type of this PublicObjectList.  # noqa: E501
        :rtype: str
        """
        return self._processing_type

    @processing_type.setter
    def processing_type(self, processing_type):
        """Sets the processing_type of this PublicObjectList.

        The processing type of the list.  # noqa: E501

        :param processing_type: The processing_type of this PublicObjectList.  # noqa: E501
        :type processing_type: str
        """
        if self.local_vars_configuration.client_side_validation and processing_type is None:  # noqa: E501
            raise ValueError("Invalid value for `processing_type`, must not be `None`")  # noqa: E501

        self._processing_type = processing_type

    @property
    def object_type_id(self):
        """Gets the object_type_id of this PublicObjectList.  # noqa: E501

        The object type of the list.  # noqa: E501

        :return: The object_type_id of this PublicObjectList.  # noqa: E501
        :rtype: str
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this PublicObjectList.

        The object type of the list.  # noqa: E501

        :param object_type_id: The object_type_id of this PublicObjectList.  # noqa: E501
        :type object_type_id: str
        """
        if self.local_vars_configuration.client_side_validation and object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_type_id`, must not be `None`")  # noqa: E501

        self._object_type_id = object_type_id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this PublicObjectList.  # noqa: E501

        The ID of the user that last updated the list.  # noqa: E501

        :return: The updated_by_id of this PublicObjectList.  # noqa: E501
        :rtype: int
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this PublicObjectList.

        The ID of the user that last updated the list.  # noqa: E501

        :param updated_by_id: The updated_by_id of this PublicObjectList.  # noqa: E501
        :type updated_by_id: int
        """

        self._updated_by_id = updated_by_id

    @property
    def filters_updated_at(self):
        """Gets the filters_updated_at of this PublicObjectList.  # noqa: E501

        The time when the filters for this list were last updated.  # noqa: E501

        :return: The filters_updated_at of this PublicObjectList.  # noqa: E501
        :rtype: datetime
        """
        return self._filters_updated_at

    @filters_updated_at.setter
    def filters_updated_at(self, filters_updated_at):
        """Sets the filters_updated_at of this PublicObjectList.

        The time when the filters for this list were last updated.  # noqa: E501

        :param filters_updated_at: The filters_updated_at of this PublicObjectList.  # noqa: E501
        :type filters_updated_at: datetime
        """

        self._filters_updated_at = filters_updated_at

    @property
    def list_id(self):
        """Gets the list_id of this PublicObjectList.  # noqa: E501

        The **ILS ID** of the list.  # noqa: E501

        :return: The list_id of this PublicObjectList.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this PublicObjectList.

        The **ILS ID** of the list.  # noqa: E501

        :param list_id: The list_id of this PublicObjectList.  # noqa: E501
        :type list_id: int
        """
        if self.local_vars_configuration.client_side_validation and list_id is None:  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501

        self._list_id = list_id

    @property
    def created_at(self):
        """Gets the created_at of this PublicObjectList.  # noqa: E501

        The time when the list was created.  # noqa: E501

        :return: The created_at of this PublicObjectList.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicObjectList.

        The time when the list was created.  # noqa: E501

        :param created_at: The created_at of this PublicObjectList.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def processing_status(self):
        """Gets the processing_status of this PublicObjectList.  # noqa: E501

        The processing status of the list.  # noqa: E501

        :return: The processing_status of this PublicObjectList.  # noqa: E501
        :rtype: str
        """
        return self._processing_status

    @processing_status.setter
    def processing_status(self, processing_status):
        """Sets the processing_status of this PublicObjectList.

        The processing status of the list.  # noqa: E501

        :param processing_status: The processing_status of this PublicObjectList.  # noqa: E501
        :type processing_status: str
        """
        if self.local_vars_configuration.client_side_validation and processing_status is None:  # noqa: E501
            raise ValueError("Invalid value for `processing_status`, must not be `None`")  # noqa: E501

        self._processing_status = processing_status

    @property
    def deleted_at(self):
        """Gets the deleted_at of this PublicObjectList.  # noqa: E501

        The time when the list was deleted.  # noqa: E501

        :return: The deleted_at of this PublicObjectList.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this PublicObjectList.

        The time when the list was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this PublicObjectList.  # noqa: E501
        :type deleted_at: datetime
        """

        self._deleted_at = deleted_at

    @property
    def list_version(self):
        """Gets the list_version of this PublicObjectList.  # noqa: E501

        The version of the list.  # noqa: E501

        :return: The list_version of this PublicObjectList.  # noqa: E501
        :rtype: int
        """
        return self._list_version

    @list_version.setter
    def list_version(self, list_version):
        """Sets the list_version of this PublicObjectList.

        The version of the list.  # noqa: E501

        :param list_version: The list_version of this PublicObjectList.  # noqa: E501
        :type list_version: int
        """
        if self.local_vars_configuration.client_side_validation and list_version is None:  # noqa: E501
            raise ValueError("Invalid value for `list_version`, must not be `None`")  # noqa: E501

        self._list_version = list_version

    @property
    def name(self):
        """Gets the name of this PublicObjectList.  # noqa: E501

        The name of the list.  # noqa: E501

        :return: The name of this PublicObjectList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicObjectList.

        The name of the list.  # noqa: E501

        :param name: The name of this PublicObjectList.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PublicObjectList.  # noqa: E501

        The ID of the user that created the list.  # noqa: E501

        :return: The created_by_id of this PublicObjectList.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PublicObjectList.

        The ID of the user that created the list.  # noqa: E501

        :param created_by_id: The created_by_id of this PublicObjectList.  # noqa: E501
        :type created_by_id: int
        """

        self._created_by_id = created_by_id

    @property
    def filter_branch(self):
        """Gets the filter_branch of this PublicObjectList.  # noqa: E501


        :return: The filter_branch of this PublicObjectList.  # noqa: E501
        :rtype: PublicPropertyAssociationFilterBranchFilterBranchesInner
        """
        return self._filter_branch

    @filter_branch.setter
    def filter_branch(self, filter_branch):
        """Sets the filter_branch of this PublicObjectList.


        :param filter_branch: The filter_branch of this PublicObjectList.  # noqa: E501
        :type filter_branch: PublicPropertyAssociationFilterBranchFilterBranchesInner
        """

        self._filter_branch = filter_branch

    @property
    def updated_at(self):
        """Gets the updated_at of this PublicObjectList.  # noqa: E501

        The time the list was last updated.  # noqa: E501

        :return: The updated_at of this PublicObjectList.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublicObjectList.

        The time the list was last updated.  # noqa: E501

        :param updated_at: The updated_at of this PublicObjectList.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, PublicObjectList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicObjectList):
            return True

        return self.to_dict() != other.to_dict()

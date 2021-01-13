# coding: utf-8

"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from MergeATSClient.configuration import Configuration


class EndUserDetails(object):
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
        'end_user_email_address': 'str',
        'end_user_organization_name': 'str',
        'end_user_origin_id': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'end_user_email_address': 'end_user_email_address',
        'end_user_organization_name': 'end_user_organization_name',
        'end_user_origin_id': 'end_user_origin_id',
        'categories': 'categories'
    }

    def __init__(self, end_user_email_address=None, end_user_organization_name=None, end_user_origin_id=None, categories=None, local_vars_configuration=None):  # noqa: E501
        """EndUserDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_user_email_address = None
        self._end_user_organization_name = None
        self._end_user_origin_id = None
        self._categories = None
        self.discriminator = None

        self.end_user_email_address = end_user_email_address
        self.end_user_organization_name = end_user_organization_name
        self.end_user_origin_id = end_user_origin_id
        self.categories = categories

    @property
    def end_user_email_address(self):
        """Gets the end_user_email_address of this EndUserDetails.  # noqa: E501


        :return: The end_user_email_address of this EndUserDetails.  # noqa: E501
        :rtype: str
        """
        return self._end_user_email_address

    @end_user_email_address.setter
    def end_user_email_address(self, end_user_email_address):
        """Sets the end_user_email_address of this EndUserDetails.


        :param end_user_email_address: The end_user_email_address of this EndUserDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and end_user_email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `end_user_email_address`, must not be `None`")  # noqa: E501

        self._end_user_email_address = end_user_email_address

    @property
    def end_user_organization_name(self):
        """Gets the end_user_organization_name of this EndUserDetails.  # noqa: E501


        :return: The end_user_organization_name of this EndUserDetails.  # noqa: E501
        :rtype: str
        """
        return self._end_user_organization_name

    @end_user_organization_name.setter
    def end_user_organization_name(self, end_user_organization_name):
        """Sets the end_user_organization_name of this EndUserDetails.


        :param end_user_organization_name: The end_user_organization_name of this EndUserDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and end_user_organization_name is None:  # noqa: E501
            raise ValueError("Invalid value for `end_user_organization_name`, must not be `None`")  # noqa: E501

        self._end_user_organization_name = end_user_organization_name

    @property
    def end_user_origin_id(self):
        """Gets the end_user_origin_id of this EndUserDetails.  # noqa: E501


        :return: The end_user_origin_id of this EndUserDetails.  # noqa: E501
        :rtype: str
        """
        return self._end_user_origin_id

    @end_user_origin_id.setter
    def end_user_origin_id(self, end_user_origin_id):
        """Sets the end_user_origin_id of this EndUserDetails.


        :param end_user_origin_id: The end_user_origin_id of this EndUserDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and end_user_origin_id is None:  # noqa: E501
            raise ValueError("Invalid value for `end_user_origin_id`, must not be `None`")  # noqa: E501

        self._end_user_origin_id = end_user_origin_id

    @property
    def categories(self):
        """Gets the categories of this EndUserDetails.  # noqa: E501


        :return: The categories of this EndUserDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this EndUserDetails.


        :param categories: The categories of this EndUserDetails.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and categories is None:  # noqa: E501
            raise ValueError("Invalid value for `categories`, must not be `None`")  # noqa: E501
        allowed_values = ["hris", "ats"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(categories).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `categories` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(categories) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._categories = categories

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, EndUserDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndUserDetails):
            return True

        return self.to_dict() != other.to_dict()

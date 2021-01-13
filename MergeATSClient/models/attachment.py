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


class Attachment(object):
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
        'id': 'str',
        'remote_id': 'str',
        'file_name': 'str',
        'file_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'file_name': 'file_name',
        'file_url': 'file_url'
    }

    def __init__(self, id=None, remote_id=None, file_name=None, file_url=None, local_vars_configuration=None):  # noqa: E501
        """Attachment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._file_name = None
        self._file_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_id = remote_id
        self.file_name = file_name
        self.file_url = file_url

    @property
    def id(self):
        """Gets the id of this Attachment.  # noqa: E501


        :return: The id of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attachment.


        :param id: The id of this Attachment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this Attachment.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this Attachment.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this Attachment.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def file_name(self):
        """Gets the file_name of this Attachment.  # noqa: E501

        The attachment's name.  # noqa: E501

        :return: The file_name of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Attachment.

        The attachment's name.  # noqa: E501

        :param file_name: The file_name of this Attachment.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_url(self):
        """Gets the file_url of this Attachment.  # noqa: E501

        The attachment's url.  # noqa: E501

        :return: The file_url of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this Attachment.

        The attachment's url.  # noqa: E501

        :param file_url: The file_url of this Attachment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_url is not None and len(file_url) > 400):
            raise ValueError("Invalid value for `file_url`, length must be less than or equal to `400`")  # noqa: E501

        self._file_url = file_url

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
        if not isinstance(other, Attachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Attachment):
            return True

        return self.to_dict() != other.to_dict()

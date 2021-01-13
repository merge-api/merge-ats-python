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


class Offer(object):
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
        'application': 'str',
        'creator': 'str',
        'remote_created_at': 'datetime',
        'closed_at': 'datetime',
        'sent_at': 'datetime',
        'start_date': 'datetime',
        'status': 'OfferStatusEnum'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'application': 'application',
        'creator': 'creator',
        'remote_created_at': 'remote_created_at',
        'closed_at': 'closed_at',
        'sent_at': 'sent_at',
        'start_date': 'start_date',
        'status': 'status'
    }

    def __init__(self, id=None, remote_id=None, application=None, creator=None, remote_created_at=None, closed_at=None, sent_at=None, start_date=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Offer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._application = None
        self._creator = None
        self._remote_created_at = None
        self._closed_at = None
        self._sent_at = None
        self._start_date = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_id = remote_id
        self.application = application
        self.creator = creator
        self.remote_created_at = remote_created_at
        self.closed_at = closed_at
        self.sent_at = sent_at
        self.start_date = start_date
        self.status = status

    @property
    def id(self):
        """Gets the id of this Offer.  # noqa: E501


        :return: The id of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Offer.


        :param id: The id of this Offer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this Offer.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this Offer.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this Offer.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def application(self):
        """Gets the application of this Offer.  # noqa: E501

        The application being for the offer.  # noqa: E501

        :return: The application of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this Offer.

        The application being for the offer.  # noqa: E501

        :param application: The application of this Offer.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def creator(self):
        """Gets the creator of this Offer.  # noqa: E501

        The user who created the offer.  # noqa: E501

        :return: The creator of this Offer.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Offer.

        The user who created the offer.  # noqa: E501

        :param creator: The creator of this Offer.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def remote_created_at(self):
        """Gets the remote_created_at of this Offer.  # noqa: E501

        When the third party's scorecard was created.  # noqa: E501

        :return: The remote_created_at of this Offer.  # noqa: E501
        :rtype: datetime
        """
        return self._remote_created_at

    @remote_created_at.setter
    def remote_created_at(self, remote_created_at):
        """Sets the remote_created_at of this Offer.

        When the third party's scorecard was created.  # noqa: E501

        :param remote_created_at: The remote_created_at of this Offer.  # noqa: E501
        :type: datetime
        """

        self._remote_created_at = remote_created_at

    @property
    def closed_at(self):
        """Gets the closed_at of this Offer.  # noqa: E501

        When the offer was closed.  # noqa: E501

        :return: The closed_at of this Offer.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this Offer.

        When the offer was closed.  # noqa: E501

        :param closed_at: The closed_at of this Offer.  # noqa: E501
        :type: datetime
        """

        self._closed_at = closed_at

    @property
    def sent_at(self):
        """Gets the sent_at of this Offer.  # noqa: E501

        When the offer was sent.  # noqa: E501

        :return: The sent_at of this Offer.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_at

    @sent_at.setter
    def sent_at(self, sent_at):
        """Sets the sent_at of this Offer.

        When the offer was sent.  # noqa: E501

        :param sent_at: The sent_at of this Offer.  # noqa: E501
        :type: datetime
        """

        self._sent_at = sent_at

    @property
    def start_date(self):
        """Gets the start_date of this Offer.  # noqa: E501

        The offered start date.  # noqa: E501

        :return: The start_date of this Offer.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Offer.

        The offered start date.  # noqa: E501

        :param start_date: The start_date of this Offer.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this Offer.  # noqa: E501

        The offer's status.  # noqa: E501

        :return: The status of this Offer.  # noqa: E501
        :rtype: OfferStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Offer.

        The offer's status.  # noqa: E501

        :param status: The status of this Offer.  # noqa: E501
        :type: OfferStatusEnum
        """

        self._status = status

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
        if not isinstance(other, Offer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Offer):
            return True

        return self.to_dict() != other.to_dict()

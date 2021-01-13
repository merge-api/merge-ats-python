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


class PatchedEEOC(object):
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
        'candidate': 'str',
        'submitted_at': 'datetime',
        'race': 'RaceEnum',
        'gender': 'GenderEnum',
        'veteran_status': 'VeteranStatusEnum',
        'disability_status': 'DisabilityStatusEnum'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'candidate': 'candidate',
        'submitted_at': 'submitted_at',
        'race': 'race',
        'gender': 'gender',
        'veteran_status': 'veteran_status',
        'disability_status': 'disability_status'
    }

    def __init__(self, id=None, remote_id=None, candidate=None, submitted_at=None, race=None, gender=None, veteran_status=None, disability_status=None, local_vars_configuration=None):  # noqa: E501
        """PatchedEEOC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._candidate = None
        self._submitted_at = None
        self._race = None
        self._gender = None
        self._veteran_status = None
        self._disability_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_id = remote_id
        self.candidate = candidate
        self.submitted_at = submitted_at
        self.race = race
        self.gender = gender
        self.veteran_status = veteran_status
        self.disability_status = disability_status

    @property
    def id(self):
        """Gets the id of this PatchedEEOC.  # noqa: E501


        :return: The id of this PatchedEEOC.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatchedEEOC.


        :param id: The id of this PatchedEEOC.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this PatchedEEOC.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this PatchedEEOC.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this PatchedEEOC.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this PatchedEEOC.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def candidate(self):
        """Gets the candidate of this PatchedEEOC.  # noqa: E501

        The candidate being represented.  # noqa: E501

        :return: The candidate of this PatchedEEOC.  # noqa: E501
        :rtype: str
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """Sets the candidate of this PatchedEEOC.

        The candidate being represented.  # noqa: E501

        :param candidate: The candidate of this PatchedEEOC.  # noqa: E501
        :type: str
        """

        self._candidate = candidate

    @property
    def submitted_at(self):
        """Gets the submitted_at of this PatchedEEOC.  # noqa: E501

        When the information was submitted.  # noqa: E501

        :return: The submitted_at of this PatchedEEOC.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this PatchedEEOC.

        When the information was submitted.  # noqa: E501

        :param submitted_at: The submitted_at of this PatchedEEOC.  # noqa: E501
        :type: datetime
        """

        self._submitted_at = submitted_at

    @property
    def race(self):
        """Gets the race of this PatchedEEOC.  # noqa: E501

        The candidate's race.  # noqa: E501

        :return: The race of this PatchedEEOC.  # noqa: E501
        :rtype: RaceEnum
        """
        return self._race

    @race.setter
    def race(self, race):
        """Sets the race of this PatchedEEOC.

        The candidate's race.  # noqa: E501

        :param race: The race of this PatchedEEOC.  # noqa: E501
        :type: RaceEnum
        """

        self._race = race

    @property
    def gender(self):
        """Gets the gender of this PatchedEEOC.  # noqa: E501

        The candidate's gender.  # noqa: E501

        :return: The gender of this PatchedEEOC.  # noqa: E501
        :rtype: GenderEnum
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PatchedEEOC.

        The candidate's gender.  # noqa: E501

        :param gender: The gender of this PatchedEEOC.  # noqa: E501
        :type: GenderEnum
        """

        self._gender = gender

    @property
    def veteran_status(self):
        """Gets the veteran_status of this PatchedEEOC.  # noqa: E501

        The candidate's veteran status.  # noqa: E501

        :return: The veteran_status of this PatchedEEOC.  # noqa: E501
        :rtype: VeteranStatusEnum
        """
        return self._veteran_status

    @veteran_status.setter
    def veteran_status(self, veteran_status):
        """Sets the veteran_status of this PatchedEEOC.

        The candidate's veteran status.  # noqa: E501

        :param veteran_status: The veteran_status of this PatchedEEOC.  # noqa: E501
        :type: VeteranStatusEnum
        """

        self._veteran_status = veteran_status

    @property
    def disability_status(self):
        """Gets the disability_status of this PatchedEEOC.  # noqa: E501

        The candidate's disability status.  # noqa: E501

        :return: The disability_status of this PatchedEEOC.  # noqa: E501
        :rtype: DisabilityStatusEnum
        """
        return self._disability_status

    @disability_status.setter
    def disability_status(self, disability_status):
        """Sets the disability_status of this PatchedEEOC.

        The candidate's disability status.  # noqa: E501

        :param disability_status: The disability_status of this PatchedEEOC.  # noqa: E501
        :type: DisabilityStatusEnum
        """

        self._disability_status = disability_status

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
        if not isinstance(other, PatchedEEOC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedEEOC):
            return True

        return self.to_dict() != other.to_dict()

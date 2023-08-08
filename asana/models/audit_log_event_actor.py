# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AuditLogEventActor(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'actor_type': 'str',
        'gid': 'str',
        'name': 'str',
        'email': 'str'
    }

    attribute_map = {
        'actor_type': 'actor_type',
        'gid': 'gid',
        'name': 'name',
        'email': 'email'
    }

    def __init__(self, actor_type=None, gid=None, name=None, email=None):  # noqa: E501
        """AuditLogEventActor - a model defined in Swagger"""  # noqa: E501
        self._actor_type = None
        self._gid = None
        self._name = None
        self._email = None
        self.discriminator = None
        if actor_type is not None:
            self.actor_type = actor_type
        if gid is not None:
            self.gid = gid
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    @property
    def actor_type(self):
        """Gets the actor_type of this AuditLogEventActor.  # noqa: E501

        The type of actor. Can be one of `user`, `asana`, `asana_support`, `anonymous`, or `external_administrator`.  # noqa: E501

        :return: The actor_type of this AuditLogEventActor.  # noqa: E501
        :rtype: str
        """
        return self._actor_type

    @actor_type.setter
    def actor_type(self, actor_type):
        """Sets the actor_type of this AuditLogEventActor.

        The type of actor. Can be one of `user`, `asana`, `asana_support`, `anonymous`, or `external_administrator`.  # noqa: E501

        :param actor_type: The actor_type of this AuditLogEventActor.  # noqa: E501
        :type: str
        """
        allowed_values = ["user", "asana", "asana_support", "anonymous", "external_administrator"]  # noqa: E501
        if actor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `actor_type` ({0}), must be one of {1}"  # noqa: E501
                .format(actor_type, allowed_values)
            )

        self._actor_type = actor_type

    @property
    def gid(self):
        """Gets the gid of this AuditLogEventActor.  # noqa: E501

        Globally unique identifier of the actor, if it is a user.  # noqa: E501

        :return: The gid of this AuditLogEventActor.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuditLogEventActor.

        Globally unique identifier of the actor, if it is a user.  # noqa: E501

        :param gid: The gid of this AuditLogEventActor.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def name(self):
        """Gets the name of this AuditLogEventActor.  # noqa: E501

        The name of the actor, if it is a user.  # noqa: E501

        :return: The name of this AuditLogEventActor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditLogEventActor.

        The name of the actor, if it is a user.  # noqa: E501

        :param name: The name of this AuditLogEventActor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this AuditLogEventActor.  # noqa: E501

        The email of the actor, if it is a user.  # noqa: E501

        :return: The email of this AuditLogEventActor.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuditLogEventActor.

        The email of the actor, if it is a user.  # noqa: E501

        :param email: The email of this AuditLogEventActor.  # noqa: E501
        :type: str
        """

        self._email = email

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AuditLogEventActor, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuditLogEventActor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
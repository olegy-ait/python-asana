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

class DateVariableCompact(object):
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
        'gid': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, gid=None, name=None, description=None):  # noqa: E501
        """DateVariableCompact - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._name = None
        self._description = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def gid(self):
        """Gets the gid of this DateVariableCompact.  # noqa: E501

        Globally unique identifier of the date field in the project template. A value of `1` refers to the project start date, while `2` refers to the project due date.  # noqa: E501

        :return: The gid of this DateVariableCompact.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this DateVariableCompact.

        Globally unique identifier of the date field in the project template. A value of `1` refers to the project start date, while `2` refers to the project due date.  # noqa: E501

        :param gid: The gid of this DateVariableCompact.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def name(self):
        """Gets the name of this DateVariableCompact.  # noqa: E501

        The name of the date variable.  # noqa: E501

        :return: The name of this DateVariableCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DateVariableCompact.

        The name of the date variable.  # noqa: E501

        :param name: The name of this DateVariableCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DateVariableCompact.  # noqa: E501

        The description of what the date variable is used for when instantiating a project.  # noqa: E501

        :return: The description of this DateVariableCompact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DateVariableCompact.

        The description of what the date variable is used for when instantiating a project.  # noqa: E501

        :param description: The description of this DateVariableCompact.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(DateVariableCompact, dict):
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
        if not isinstance(other, DateVariableCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class CustomFieldRequest(object):
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
        'resource_type': 'str',
        'name': 'str',
        'resource_subtype': 'str',
        'type': 'str',
        'enum_options': 'list[CustomFieldBaseEnumOptions]',
        'enabled': 'bool',
        'is_formula_field': 'bool',
        'date_value': 'CustomFieldBaseDateValue',
        'enum_value': 'CustomFieldBaseEnumValue',
        'multi_enum_values': 'list[CustomFieldBaseEnumOptions]',
        'number_value': 'float',
        'text_value': 'str',
        'display_value': 'str',
        'description': 'str',
        'precision': 'int',
        'format': 'str',
        'currency_code': 'str',
        'custom_label': 'str',
        'custom_label_position': 'str',
        'is_global_to_workspace': 'bool',
        'has_notifications_enabled': 'bool',
        'asana_created_field': 'str',
        'workspace': 'str',
        'owned_by_app': 'bool',
        'people_value': 'list[str]'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'name': 'name',
        'resource_subtype': 'resource_subtype',
        'type': 'type',
        'enum_options': 'enum_options',
        'enabled': 'enabled',
        'is_formula_field': 'is_formula_field',
        'date_value': 'date_value',
        'enum_value': 'enum_value',
        'multi_enum_values': 'multi_enum_values',
        'number_value': 'number_value',
        'text_value': 'text_value',
        'display_value': 'display_value',
        'description': 'description',
        'precision': 'precision',
        'format': 'format',
        'currency_code': 'currency_code',
        'custom_label': 'custom_label',
        'custom_label_position': 'custom_label_position',
        'is_global_to_workspace': 'is_global_to_workspace',
        'has_notifications_enabled': 'has_notifications_enabled',
        'asana_created_field': 'asana_created_field',
        'workspace': 'workspace',
        'owned_by_app': 'owned_by_app',
        'people_value': 'people_value'
    }

    def __init__(self, gid=None, resource_type=None, name=None, resource_subtype=None, type=None, enum_options=None, enabled=None, is_formula_field=None, date_value=None, enum_value=None, multi_enum_values=None, number_value=None, text_value=None, display_value=None, description=None, precision=None, format=None, currency_code=None, custom_label=None, custom_label_position=None, is_global_to_workspace=None, has_notifications_enabled=None, asana_created_field=None, workspace=None, owned_by_app=None, people_value=None):  # noqa: E501
        """CustomFieldRequest - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._name = None
        self._resource_subtype = None
        self._type = None
        self._enum_options = None
        self._enabled = None
        self._is_formula_field = None
        self._date_value = None
        self._enum_value = None
        self._multi_enum_values = None
        self._number_value = None
        self._text_value = None
        self._display_value = None
        self._description = None
        self._precision = None
        self._format = None
        self._currency_code = None
        self._custom_label = None
        self._custom_label_position = None
        self._is_global_to_workspace = None
        self._has_notifications_enabled = None
        self._asana_created_field = None
        self._workspace = None
        self._owned_by_app = None
        self._people_value = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if name is not None:
            self.name = name
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype
        if type is not None:
            self.type = type
        if enum_options is not None:
            self.enum_options = enum_options
        if enabled is not None:
            self.enabled = enabled
        if is_formula_field is not None:
            self.is_formula_field = is_formula_field
        if date_value is not None:
            self.date_value = date_value
        if enum_value is not None:
            self.enum_value = enum_value
        if multi_enum_values is not None:
            self.multi_enum_values = multi_enum_values
        if number_value is not None:
            self.number_value = number_value
        if text_value is not None:
            self.text_value = text_value
        if display_value is not None:
            self.display_value = display_value
        if description is not None:
            self.description = description
        if precision is not None:
            self.precision = precision
        if format is not None:
            self.format = format
        if currency_code is not None:
            self.currency_code = currency_code
        if custom_label is not None:
            self.custom_label = custom_label
        if custom_label_position is not None:
            self.custom_label_position = custom_label_position
        if is_global_to_workspace is not None:
            self.is_global_to_workspace = is_global_to_workspace
        if has_notifications_enabled is not None:
            self.has_notifications_enabled = has_notifications_enabled
        if asana_created_field is not None:
            self.asana_created_field = asana_created_field
        self.workspace = workspace
        if owned_by_app is not None:
            self.owned_by_app = owned_by_app
        if people_value is not None:
            self.people_value = people_value

    @property
    def gid(self):
        """Gets the gid of this CustomFieldRequest.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this CustomFieldRequest.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this CustomFieldRequest.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CustomFieldRequest.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this CustomFieldRequest.  # noqa: E501

        The name of the custom field.  # noqa: E501

        :return: The name of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomFieldRequest.

        The name of the custom field.  # noqa: E501

        :param name: The name of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this CustomFieldRequest.  # noqa: E501

        The type of the custom field. Must be one of the given values.   # noqa: E501

        :return: The resource_subtype of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this CustomFieldRequest.

        The type of the custom field. Must be one of the given values.   # noqa: E501

        :param resource_subtype: The resource_subtype of this CustomFieldRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "enum", "multi_enum", "number", "date", "people"]  # noqa: E501
        if resource_subtype not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_subtype` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_subtype, allowed_values)
            )

        self._resource_subtype = resource_subtype

    @property
    def type(self):
        """Gets the type of this CustomFieldRequest.  # noqa: E501

        *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.   # noqa: E501

        :return: The type of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomFieldRequest.

        *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.   # noqa: E501

        :param type: The type of this CustomFieldRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "enum", "multi_enum", "number", "date", "people"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def enum_options(self):
        """Gets the enum_options of this CustomFieldRequest.  # noqa: E501

        *Conditional*. Only relevant for custom fields of type `enum`. This array specifies the possible values which an `enum` custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield).  # noqa: E501

        :return: The enum_options of this CustomFieldRequest.  # noqa: E501
        :rtype: list[CustomFieldBaseEnumOptions]
        """
        return self._enum_options

    @enum_options.setter
    def enum_options(self, enum_options):
        """Sets the enum_options of this CustomFieldRequest.

        *Conditional*. Only relevant for custom fields of type `enum`. This array specifies the possible values which an `enum` custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield).  # noqa: E501

        :param enum_options: The enum_options of this CustomFieldRequest.  # noqa: E501
        :type: list[CustomFieldBaseEnumOptions]
        """

        self._enum_options = enum_options

    @property
    def enabled(self):
        """Gets the enabled of this CustomFieldRequest.  # noqa: E501

        *Conditional*. Determines if the custom field is enabled or not.  # noqa: E501

        :return: The enabled of this CustomFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CustomFieldRequest.

        *Conditional*. Determines if the custom field is enabled or not.  # noqa: E501

        :param enabled: The enabled of this CustomFieldRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def is_formula_field(self):
        """Gets the is_formula_field of this CustomFieldRequest.  # noqa: E501

        *Conditional*. This flag describes whether a custom field is a formula custom field.  # noqa: E501

        :return: The is_formula_field of this CustomFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_formula_field

    @is_formula_field.setter
    def is_formula_field(self, is_formula_field):
        """Sets the is_formula_field of this CustomFieldRequest.

        *Conditional*. This flag describes whether a custom field is a formula custom field.  # noqa: E501

        :param is_formula_field: The is_formula_field of this CustomFieldRequest.  # noqa: E501
        :type: bool
        """

        self._is_formula_field = is_formula_field

    @property
    def date_value(self):
        """Gets the date_value of this CustomFieldRequest.  # noqa: E501


        :return: The date_value of this CustomFieldRequest.  # noqa: E501
        :rtype: CustomFieldBaseDateValue
        """
        return self._date_value

    @date_value.setter
    def date_value(self, date_value):
        """Sets the date_value of this CustomFieldRequest.


        :param date_value: The date_value of this CustomFieldRequest.  # noqa: E501
        :type: CustomFieldBaseDateValue
        """

        self._date_value = date_value

    @property
    def enum_value(self):
        """Gets the enum_value of this CustomFieldRequest.  # noqa: E501


        :return: The enum_value of this CustomFieldRequest.  # noqa: E501
        :rtype: CustomFieldBaseEnumValue
        """
        return self._enum_value

    @enum_value.setter
    def enum_value(self, enum_value):
        """Sets the enum_value of this CustomFieldRequest.


        :param enum_value: The enum_value of this CustomFieldRequest.  # noqa: E501
        :type: CustomFieldBaseEnumValue
        """

        self._enum_value = enum_value

    @property
    def multi_enum_values(self):
        """Gets the multi_enum_values of this CustomFieldRequest.  # noqa: E501

        *Conditional*. Only relevant for custom fields of type `multi_enum`. This object is the chosen values of a `multi_enum` custom field.  # noqa: E501

        :return: The multi_enum_values of this CustomFieldRequest.  # noqa: E501
        :rtype: list[CustomFieldBaseEnumOptions]
        """
        return self._multi_enum_values

    @multi_enum_values.setter
    def multi_enum_values(self, multi_enum_values):
        """Sets the multi_enum_values of this CustomFieldRequest.

        *Conditional*. Only relevant for custom fields of type `multi_enum`. This object is the chosen values of a `multi_enum` custom field.  # noqa: E501

        :param multi_enum_values: The multi_enum_values of this CustomFieldRequest.  # noqa: E501
        :type: list[CustomFieldBaseEnumOptions]
        """

        self._multi_enum_values = multi_enum_values

    @property
    def number_value(self):
        """Gets the number_value of this CustomFieldRequest.  # noqa: E501

        *Conditional*. This number is the value of a `number` custom field.  # noqa: E501

        :return: The number_value of this CustomFieldRequest.  # noqa: E501
        :rtype: float
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this CustomFieldRequest.

        *Conditional*. This number is the value of a `number` custom field.  # noqa: E501

        :param number_value: The number_value of this CustomFieldRequest.  # noqa: E501
        :type: float
        """

        self._number_value = number_value

    @property
    def text_value(self):
        """Gets the text_value of this CustomFieldRequest.  # noqa: E501

        *Conditional*. This string is the value of a `text` custom field.  # noqa: E501

        :return: The text_value of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """Sets the text_value of this CustomFieldRequest.

        *Conditional*. This string is the value of a `text` custom field.  # noqa: E501

        :param text_value: The text_value of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._text_value = text_value

    @property
    def display_value(self):
        """Gets the display_value of this CustomFieldRequest.  # noqa: E501

        A string representation for the value of the custom field. Integrations that don't require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types.  # noqa: E501

        :return: The display_value of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """Sets the display_value of this CustomFieldRequest.

        A string representation for the value of the custom field. Integrations that don't require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types.  # noqa: E501

        :param display_value: The display_value of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._display_value = display_value

    @property
    def description(self):
        """Gets the description of this CustomFieldRequest.  # noqa: E501

        [Opt In](/docs/inputoutput-options). The description of the custom field.  # noqa: E501

        :return: The description of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomFieldRequest.

        [Opt In](/docs/inputoutput-options). The description of the custom field.  # noqa: E501

        :param description: The description of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def precision(self):
        """Gets the precision of this CustomFieldRequest.  # noqa: E501

        Only relevant for custom fields of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%. The identifier format will always have a precision of 0.  # noqa: E501

        :return: The precision of this CustomFieldRequest.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this CustomFieldRequest.

        Only relevant for custom fields of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%. The identifier format will always have a precision of 0.  # noqa: E501

        :param precision: The precision of this CustomFieldRequest.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def format(self):
        """Gets the format of this CustomFieldRequest.  # noqa: E501

        The format of this custom field.  # noqa: E501

        :return: The format of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CustomFieldRequest.

        The format of this custom field.  # noqa: E501

        :param format: The format of this CustomFieldRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["currency", "identifier", "percentage", "custom", "duration", "none"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def currency_code(self):
        """Gets the currency_code of this CustomFieldRequest.  # noqa: E501

        ISO 4217 currency code to format this custom field. This will be null if the `format` is not `currency`.  # noqa: E501

        :return: The currency_code of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CustomFieldRequest.

        ISO 4217 currency code to format this custom field. This will be null if the `format` is not `currency`.  # noqa: E501

        :param currency_code: The currency_code of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def custom_label(self):
        """Gets the custom_label of this CustomFieldRequest.  # noqa: E501

        This is the string that appears next to the custom field value. This will be null if the `format` is not `custom`.  # noqa: E501

        :return: The custom_label of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_label

    @custom_label.setter
    def custom_label(self, custom_label):
        """Sets the custom_label of this CustomFieldRequest.

        This is the string that appears next to the custom field value. This will be null if the `format` is not `custom`.  # noqa: E501

        :param custom_label: The custom_label of this CustomFieldRequest.  # noqa: E501
        :type: str
        """

        self._custom_label = custom_label

    @property
    def custom_label_position(self):
        """Gets the custom_label_position of this CustomFieldRequest.  # noqa: E501

        Only relevant for custom fields with `custom` format. This depicts where to place the custom label. This will be null if the `format` is not `custom`.  # noqa: E501

        :return: The custom_label_position of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_label_position

    @custom_label_position.setter
    def custom_label_position(self, custom_label_position):
        """Sets the custom_label_position of this CustomFieldRequest.

        Only relevant for custom fields with `custom` format. This depicts where to place the custom label. This will be null if the `format` is not `custom`.  # noqa: E501

        :param custom_label_position: The custom_label_position of this CustomFieldRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["prefix", "suffix", ""]  # noqa: E501
        if custom_label_position not in allowed_values:
            raise ValueError(
                "Invalid value for `custom_label_position` ({0}), must be one of {1}"  # noqa: E501
                .format(custom_label_position, allowed_values)
            )

        self._custom_label_position = custom_label_position

    @property
    def is_global_to_workspace(self):
        """Gets the is_global_to_workspace of this CustomFieldRequest.  # noqa: E501

        This flag describes whether this custom field is available to every container in the workspace. Before project-specific custom fields, this field was always true.  # noqa: E501

        :return: The is_global_to_workspace of this CustomFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_global_to_workspace

    @is_global_to_workspace.setter
    def is_global_to_workspace(self, is_global_to_workspace):
        """Sets the is_global_to_workspace of this CustomFieldRequest.

        This flag describes whether this custom field is available to every container in the workspace. Before project-specific custom fields, this field was always true.  # noqa: E501

        :param is_global_to_workspace: The is_global_to_workspace of this CustomFieldRequest.  # noqa: E501
        :type: bool
        """

        self._is_global_to_workspace = is_global_to_workspace

    @property
    def has_notifications_enabled(self):
        """Gets the has_notifications_enabled of this CustomFieldRequest.  # noqa: E501

        *Conditional*. This flag describes whether a follower of a task with this field should receive inbox notifications from changes to this field.  # noqa: E501

        :return: The has_notifications_enabled of this CustomFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_notifications_enabled

    @has_notifications_enabled.setter
    def has_notifications_enabled(self, has_notifications_enabled):
        """Sets the has_notifications_enabled of this CustomFieldRequest.

        *Conditional*. This flag describes whether a follower of a task with this field should receive inbox notifications from changes to this field.  # noqa: E501

        :param has_notifications_enabled: The has_notifications_enabled of this CustomFieldRequest.  # noqa: E501
        :type: bool
        """

        self._has_notifications_enabled = has_notifications_enabled

    @property
    def asana_created_field(self):
        """Gets the asana_created_field of this CustomFieldRequest.  # noqa: E501

        *Conditional*. A unique identifier to associate this field with the template source of truth.  # noqa: E501

        :return: The asana_created_field of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._asana_created_field

    @asana_created_field.setter
    def asana_created_field(self, asana_created_field):
        """Sets the asana_created_field of this CustomFieldRequest.

        *Conditional*. A unique identifier to associate this field with the template source of truth.  # noqa: E501

        :param asana_created_field: The asana_created_field of this CustomFieldRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["a_v_requirements", "account_name", "actionable", "align_shipping_link", "align_status", "allotted_time", "appointment", "approval_stage", "approved", "article_series", "board_committee", "browser", "campaign_audience", "campaign_project_status", "campaign_regions", "channel_primary", "client_topic_type", "complete_by", "contact", "contact_email_address", "content_channels", "content_channels_needed", "content_stage", "content_type", "contract", "contract_status", "cost", "creation_stage", "creative_channel", "creative_needed", "creative_needs", "data_sensitivity", "deal_size", "delivery_appt", "delivery_appt_date", "department", "department_responsible", "design_request_needed", "design_request_type", "discussion_category", "do_this_task", "editorial_content_status", "editorial_content_tag", "editorial_content_type", "effort", "effort_level", "est_completion_date", "estimated_time", "estimated_value", "expected_cost", "external_steps_needed", "favorite_idea", "feedback_type", "financial", "funding_amount", "grant_application_process", "hiring_candidate_status", "idea_status", "ids_link", "ids_patient_link", "implementation_stage", "insurance", "interview_area", "interview_question_score", "itero_scan_link", "job_s_applied_to", "lab", "launch_status", "lead_status", "localization_language", "localization_market_team", "localization_status", "meeting_minutes", "meeting_needed", "minutes", "mrr", "must_localize", "name_of_foundation", "need_to_follow_up", "next_appointment", "next_steps_sales", "num_people", "number_of_user_reports", "office_location", "onboarding_activity", "owner", "participants_needed", "patient_date_of_birth", "patient_email", "patient_phone", "patient_status", "phone_number", "planning_category", "point_of_contact", "position", "post_format", "prescription", "priority", "priority_level", "product", "product_stage", "progress", "project_size", "project_status", "proposed_budget", "publish_status", "reason_for_scan", "referral", "request_type", "research_status", "responsible_department", "responsible_team", "risk_assessment_status", "room_name", "sales_counterpart", "sentiment", "shipping_link", "social_channels", "stage", "status", "status_design", "status_of_initiative", "system_setup", "task_progress", "team", "team_marketing", "team_responsible", "time_it_takes_to_complete_tasks", "timeframe", "treatment_type", "type_work_requests_it", "use_agency", "user_name", "vendor_category", "vendor_type", "word_count", ""]  # noqa: E501
        if asana_created_field not in allowed_values:
            raise ValueError(
                "Invalid value for `asana_created_field` ({0}), must be one of {1}"  # noqa: E501
                .format(asana_created_field, allowed_values)
            )

        self._asana_created_field = asana_created_field

    @property
    def workspace(self):
        """Gets the workspace of this CustomFieldRequest.  # noqa: E501

        *Create-Only* The workspace to create a custom field in.  # noqa: E501

        :return: The workspace of this CustomFieldRequest.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this CustomFieldRequest.

        *Create-Only* The workspace to create a custom field in.  # noqa: E501

        :param workspace: The workspace of this CustomFieldRequest.  # noqa: E501
        :type: str
        """
        if workspace is None:
            raise ValueError("Invalid value for `workspace`, must not be `None`")  # noqa: E501

        self._workspace = workspace

    @property
    def owned_by_app(self):
        """Gets the owned_by_app of this CustomFieldRequest.  # noqa: E501

        *Allow-listed*. Instructs the API that this Custom Field is app-owned. This parameter is allow-listed to specific apps at this point in time. For apps that are not allow-listed, providing this parameter will result in a `403 Forbidden`.  # noqa: E501

        :return: The owned_by_app of this CustomFieldRequest.  # noqa: E501
        :rtype: bool
        """
        return self._owned_by_app

    @owned_by_app.setter
    def owned_by_app(self, owned_by_app):
        """Sets the owned_by_app of this CustomFieldRequest.

        *Allow-listed*. Instructs the API that this Custom Field is app-owned. This parameter is allow-listed to specific apps at this point in time. For apps that are not allow-listed, providing this parameter will result in a `403 Forbidden`.  # noqa: E501

        :param owned_by_app: The owned_by_app of this CustomFieldRequest.  # noqa: E501
        :type: bool
        """

        self._owned_by_app = owned_by_app

    @property
    def people_value(self):
        """Gets the people_value of this CustomFieldRequest.  # noqa: E501

        *Conditional*. Only relevant for custom fields of type `people`. This array of user GIDs reflects the users to be written to a `people` custom field. Note that *write* operations will replace existing users (if any) in the custom field with the users specified in this array.  # noqa: E501

        :return: The people_value of this CustomFieldRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._people_value

    @people_value.setter
    def people_value(self, people_value):
        """Sets the people_value of this CustomFieldRequest.

        *Conditional*. Only relevant for custom fields of type `people`. This array of user GIDs reflects the users to be written to a `people` custom field. Note that *write* operations will replace existing users (if any) in the custom field with the users specified in this array.  # noqa: E501

        :param people_value: The people_value of this CustomFieldRequest.  # noqa: E501
        :type: list[str]
        """

        self._people_value = people_value

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
        if issubclass(CustomFieldRequest, dict):
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
        if not isinstance(other, CustomFieldRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
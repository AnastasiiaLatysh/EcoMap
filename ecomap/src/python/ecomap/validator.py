"""Validator module.
   Contains function to validate different forms in browser.
"""
import re

ENUM = {'action': ['post', 'get', 'put', 'delete'],
        'modifier': ['any', 'own', 'none']}
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$')
LENGTHS = {'email': [5, 100],
           'first_name': [2, 255],
           'last_name': [2, 255],
           'password': [6, 100],
           'pass_confirm': [6, 100],
           'resource_name': [2, 100],
           'role_name': [2, 255],
           'description': [2, 255]}

MESSAGE = {'is_in_dictionary': 'not contain %s key.',
           'is_enough_length': '%s value it too long or short.',
           'is_not_empty': '%s field is empty.',
           'is_string': '%s value is not string.',
           'is_email': '%s value does not look like email.',
           'is_in_enum': 'invalid %s value'}


def user_registration(data):
    """Validates user registration form. Checks: email, password,
       confirm password, first name, last name.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['email', 'first_name', 'last_name', 'password', 'pass_confirm']

    for key in keys:
        error_message = validate_int(data, key)
        if not error_message:
            error_message = validate_string(data, key, LENGTHS[key][0],
                                            LENGTHS[key][1])
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def user_login(data):
    """Validates user login form. Checks: email and password.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['email', 'password']

    for key in keys:
        error_message = validate_int(data, key)
        if not error_message:
            error_message = validate_string(data, key, LENGTHS[key][0],
                                            LENGTHS[key][1])
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def resource_post(data):
    """Validates resource post form. Checks: name of resource.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'resource_name'

    error_message = validate_int(data, key)
    if not error_message:
        error_message = validate_string(data, key, LENGTHS[key][0],
                                        LENGTHS[key][1])
    if error_message:
        status['error'].append(error_message)
        status['status'] = False

    return status


def resource_put(data):
    """Validates resource put form. Checks: name and id of
       resource.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['resource_name', 'resource_id']

    for key in keys:
        error_message = validate_int(data, key)
        if not error_message and key == 'resource_name':
            error_message = validate_string(data, key, LENGTHS[key][0],
                                            LENGTHS[key][1])
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def resource_delete(data):
    """Validates resource delete form. Checks: id of resource.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'resource_id'

    error_message = validate_int(data, key)
    if error_message:
        status['error'].append(error_message)
        status['status'] = False

    return status


def role_post(data):
    """Validates role post form. Checks: name of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'role_name'

    error_message = validate_int(data, key)
    if not error_message:
        error_message = validate_string(data, key, LENGTHS[key][0],
                                        LENGTHS[key][1])
    if error_message:
        status['status'] = False
        status['error'].append(error_message)

    return status


def role_put(data):
    """Validates role put form. Checks: id and name of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['role_id', 'role_name']

    for key in keys:
        error_message = validate_int(data, key)
        if not error_message and key == 'role_name':
            error_message = validate_string(data, key, LENGTHS[key][0],
                                            LENGTHS[key][1])
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def role_delete(data):
    """Validates role delete form. Checks: id of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'role_id'

    error_message = validate_int(data, key)
    if error_message:
        status['status'] = False
        status['error'].append(error_message)

    return status


def permission_post(data):
    """Validates permission post form. Checks: id of resource and
       action (POST, PUT, GET, DELETE), modifier (Any, Own, None)
       and description of permission.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['resource_id', 'action', 'modifier', 'description']

    for key in keys:
        error_message = validate_int(data, key)
        if not error_message and key in ['action', 'modifier']:
            error_message = validate_enum(data, key, ENUM[key])
        if not error_message and key == 'description':
            error_message = validate_string(data, key, LENGTHS[key][0],
                                            LENGTHS[key][1])
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def permission_put(data):
    """Validates permission put form. Checks: id of resource and
       action (POST, PUT, GET, DELETE), modifier (Any, Own, None)
       and description of permission.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['permission_id', 'action', 'modifier', 'description']

    for key in keys:
        error_message = validate_int(data, key)
        if not error_message and key in ['action', 'modifier']:
            error_message = validate_enum(data, key, ENUM[key])
        if not error_message and key == 'description':
            error_message = validate_string(data, key, LENGTHS[key][0],
                                            LENGTHS[key][1])
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def permission_delete(data):
    """Validates permission delete form. Checks: id of permission.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'permission_id'

    error_message = validate_int(data, key)
    if error_message:
        status['status'] = False
        status['error'].append(error_message)

    return status


def role_permission_post(data):
    """Validates role permission post form. Checks: id of permission
       and id of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['role_id', 'permission_id']

    for key in keys:
        error_message = validate_int(data, key)
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def role_permission_put(data):
    """Validates role permission put form. Checks: id of permission
       and id of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    return role_permission_post(data)


def role_permission_delete(data):
    """Validates role permission delete form. Checks: id of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'role_id'

    error_message = validate_int(data, key)
    if error_message:
        status['status'] = False
        status['error'].append(error_message)

    return status


def user_role_put(data):
    """Validates user role post form. Checks: id of user
       and id of role.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    keys = ['role_id', 'user_id']

    for key in keys:
        error_message = validate_int(data, key)
        if error_message:
            status['error'].append(error_message)

    if len(status['error']):
        status['status'] = False

    return status


def change_password(data):
    """Validates change user password form. Checks old password,
       new password and id of user.
       :params: data - json object
       :return: dictionary with status key and error keys. By
                default status is True, and error is empty.
                If validation failed, status changes to False
                and error key saves error message
    """
    status = {'status': True, 'error': []}
    key = 'password'

    error_message = validate_int(data, key)
    if not error_message:
        error_message = validate_string(data, key, LENGTHS[key][0],
                                        LENGTHS[key][1])
    if error_message:
        status['error'].append(error_message)
        status['status'] = False

    return status


def validate_string(data, key, minimum=0, maximum=0):
    """Function to validate string values.
       :params: data - json object
                key - json key
                min - minimal length of value
                max - maximum length of value
       :return: error message - if not passed validation
                None - if passed
    """
    result = None
    if not is_string(data, key):
        result = MESSAGE['is_string'] % key
    elif not is_enough_length(data, key, minimum, maximum):
        result = MESSAGE['is_enough_length'] % key
    elif key == 'email' and not is_email(data, key):
        result = MESSAGE['is_email'] % key
    return result


def validate_enum(data, key, enum):
    """Function to validate enum values.
       :params: data - json object
                key - json key
                enum - list of allowed values
       :return: error message - if not passed validation
                None - if passed
    """
    result = None
    if not is_in_dictionary(data, key):
        result = MESSAGE['is_in_dictionary'] % key
    elif not is_not_empty(data, key):
        result = MESSAGE['is_not_empty'] % key
    elif not is_in_enum(data, key, enum):
        result = MESSAGE['is_in_enum'] % key
    return result


def validate_int(data, key):
    """Function to validate id values.
       :params: data - json object
                key - json key
       :return: error message - if not passed validation
                None - if passed
    """
    result = None
    if not is_in_dictionary(data, key):
        result = MESSAGE['is_in_dictionary'] % key
    elif not is_not_empty(data, key):
        result = MESSAGE['is_not_empty'] % key
    return result


def is_in_dictionary(json, key):
    """Validator function, which checks if there is all needed keys json
       object.
       :params: json - json dictionary we want to check
                key - key, we expect to get from json
       :return: True - if all is ok
                False - if there is no expected key
    """
    return key in json


def is_enough_length(json, key, minimum, maximum):
    """Validator function, which checks if our string is longer than
       minimal value and shorted than maximum value.
       :params: json - JSON dictionary
                key - JSON key
                min - minimal length of string
                max - maximum length of string
       :return: True - if length of string is between min and max lengths
                False - if not
    """
    result = True
    if minimum:
        result = len(json[key]) >= minimum
    if result and maximum:
        result = len(json[key]) <= maximum
    return result


def is_email(json, key):
    """Validator function, which checks if string is similar to email.
       Uses regular expression pattern, declared above.
       :params: json - JSON dictionary
                key - JSON key
       :return: True - if string is similar to pattern
                False - if not
    """
    return EMAIL_PATTERN.match(json[key])


def is_not_empty(json, key):
    """Validator function which checks if value in json key is not empty.
       :params: json - JSON dictionary
                key - JSON key
       :return: True - if json value is not empty
                False - if it is empty
    """
    return json[key]


def is_string(json, key):
    """Validator function which checks if json value is string.
       :params: json - JSON dictionary
                key - JSON key
       :return: True - if value is string
                False - if it is not
    """
    return isinstance(json[key], basestring)


def is_in_enum(json, key, enum):
    """Validator function which checks if json value is in enum.
       :params: json - JSON dictionary
                key - JSON key
                enum - list of values
       :return: True - if value in enum
                False - if it is not
    """
    return json[key].lower() in enum

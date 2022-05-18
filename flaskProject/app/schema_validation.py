signup_validate = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'},
        'lname': {'type': 'string'},
        'fname': {'type': 'string'},
    },
    'required': ['username', 'password', 'lname', 'fname'],
}
login_validate = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'},
    },
    'required': ['email', 'password'],
}

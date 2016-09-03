schema = {
    'username': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'email': {
        'type': 'string',
        'required': True,
        'unique': True
    }
}

domain = {
    'schema': schema
}

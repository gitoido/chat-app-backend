import datetime

schema = {
    'body': {
        'type': 'string',
        'required': True
    },
    'created_at': {
        'type': 'datetime',
        'default': datetime.datetime.now()
    },
    'updated_at': {
        'type': 'datetime',
        'default': datetime.datetime.now()
    },
    'owner': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'users',
            'field': '_id',
            'embeddable': True
        }
    }
}

domain = {
    'schema': schema
}

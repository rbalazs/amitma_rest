MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'amitma_task'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DATE_FORMAT = '%Y-%m-%d'

IF_MATCH = False

X_DOMAINS = '*'

schema = {
    'musthave': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 500,
    },
    'shouldhave': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 500,
    },
    'nicetohave': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 500,
    },
    'day': {
        'type': 'datetime',
    },
}

task = {
    'item_title': 'task',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema,
    'additional_lookup': {
        'url': 'regex("\d{4}-\d{2}-\d{2}")',
        'field': 'day'
    },
}

DOMAIN = {'task': task}

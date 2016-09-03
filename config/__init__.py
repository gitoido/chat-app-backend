import os
import domain
import swagger

app = {
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    'DEBUG': True,
    'SWAGGER_INFO': swagger.api_doc_info,
    'MONGO_URI': os.getenv('MONGO_URI'),
    'ELASTICSEARCH_INDEX': 'chat',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'X_DOMAINS': '*',
    'DOMAIN': domain.domain,
}

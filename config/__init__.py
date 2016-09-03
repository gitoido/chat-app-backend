import os
import domain
import swagger

app = {
    'SWAGGER_INFO': swagger.api_doc_info,
    'ELASTICSEARCH_URL': os.getenv('BONSAI_URL', 'http://localhost:9200/'),
    'ELASTICSEARCH_INDEX': 'chat',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'X_DOMAINS': '*',
    'DOMAIN': domain.domain,
}

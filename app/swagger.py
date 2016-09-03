from flask import Blueprint
from eve_swagger.swagger import index as eve_swagger_index
from decorators import crossdomain

swagger = Blueprint('api_swagger', __name__)


@swagger.route('/api-docs')
@crossdomain(origin='*')
def index():
    return eve_swagger_index()

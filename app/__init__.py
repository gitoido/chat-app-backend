from eve import Eve
from eve_elastic import Elastic
from eve_swagger import swagger
from eve_auth_jwt import JWTAuth
import config

app = Eve(settings=config.app, data=Elastic)
app.register_blueprint(swagger)

if __name__ == '__main__':
    app.run()

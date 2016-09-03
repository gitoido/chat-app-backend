from eve import Eve
from eve_elastic import Elastic
from app.swagger import swagger
# from eve_auth_jwt import JWTAuth
from api.hooks import append_hooks

import config


app = Eve(settings=config.app, data=Elastic)
app.register_blueprint(swagger)

if __name__ == '__main__':
    append_hooks(app).run()

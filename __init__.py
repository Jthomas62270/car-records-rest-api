from flask import Flask 

def create_app(config_object=None): 
    app = Flask(__name__)
    app.config.from_object(config_object or Config)

    from .extenstion import mongo, cors 
    mongo.init_app(app)
    cors.init_app(app)

    return app

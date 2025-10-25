import os 

class BaseConfig: 
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:2701/cardb')

class DevConfig: 
    DEBUG = True

class ProdConfig(BaseConfig): 
    DEBUG = False

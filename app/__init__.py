from flask import Flask
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager

import pymongo

def create_app():
        
    app = Flask(__name__)

    # app.config['MONGODB_SETTINGS'] = {
    #     'db': '',
    #     'host': 'mongodb://<---YOUR_DB_FULL URI--->'
    # }

    app.config['MONGODB_SETTINGS'] = {
        'db':'db_name',
        'host':'localhost'
    }

    app.static_folder = 'assets'

    db = MongoEngine(app)

    # init SQLAlchemy so we can use it later in our models
    connection = pymongo.MongoClient('mongodb://localhost:27017')
    dbd = connection['bmi']
    
    #app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    return app, db, dbd, login_manager

app, db, dbd, login_manager = create_app()

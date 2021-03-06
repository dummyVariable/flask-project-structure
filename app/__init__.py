from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from app.main import main as main_blueprint
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)
    
    app.register_blueprint(main_blueprint)

    return app
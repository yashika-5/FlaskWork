from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

###################################################
################## DATABASE SET UP #################
####################################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

######## LOGIN SET UP ######
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


from peoplecompanyblog.core.views import core
app.register_blueprint(core)

from peoplecompanyblog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)
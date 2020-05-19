from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '67fb67c6df25a7438daab85e8f581f80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root''@localhost/flasklogin'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginmanager = LoginManager(app)
loginmanager.login_view = 'login'
loginmanager.login_message_category = 'info'

from flaskblock import routs

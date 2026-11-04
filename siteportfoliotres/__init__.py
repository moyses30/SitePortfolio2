
from flask import Flask , render_template ,url_for ,request ,flash ,redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']= '6311cd5b4099931e9dc7624bc309610e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db' # nome do banco

database= SQLAlchemy(app)

from siteportfoliotres import routes
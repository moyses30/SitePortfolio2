
from flask import Flask , render_template ,url_for ,request ,flash ,redirect
from flask_sqlalchemy import SQLAlchemy
import os
import sqlalchemy


app = Flask(__name__)
app.config['SECRET_KEY']= '6311cd5b4099931e9dc7624bc309610e'

if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI']= os.getenv("DATABASE_URL")

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db' # nome do banco

database= SQLAlchemy(app)

from siteportfoliotres import models
from sqlalchemy import inspect
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'] )
inspector = inspect(engine)
if not inspector.has_table('emailBancoDados'):
    with app.app_context():

        database.create_all()
        print("base criada")

else:

    print('Base existente')
from siteportfoliotres import routes
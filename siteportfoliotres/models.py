from main import database
from datetime import datetime




class EmailBancoDados(database.Model) :
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    telefone = database.Column(database.Integer,nullable= False)
    suamensagem = database.Column(database.Text,nullable =False)
    data_envio = database.Column(database.DateTime, default=datetime.utcnow)
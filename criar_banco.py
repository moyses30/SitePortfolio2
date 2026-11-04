from siteportfoliotres import  app ,database
from siteportfoliotres .models import EmailBancoDados # criação do banco de dados

with app.app_context():
     database.create_all()
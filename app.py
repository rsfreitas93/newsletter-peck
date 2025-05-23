from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# Carrega a API Key de uma variável de ambiente
load_dotenv()
googleKey = os.getenv('GOOGLE_API_KEY')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'news.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importa as rotas DEPOIS da inicialização do 'app' e 'db'
from routes.views import *
from routes.ia import *
from routes.bd import *

if __name__ == "__main__":
    app.run(debug=True)
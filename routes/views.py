from app import app
from flask import render_template

# Rota para a página inicial
@app.route("/")
def homepage():
    return render_template("index.html")
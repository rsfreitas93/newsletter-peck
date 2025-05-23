from app import app, db 
from models import News
from flask import render_template, jsonify, request

# Rota para a página inicial
@app.route("/")
def homepage():
    return render_template("index.html")

# Nova rota API para buscar notícias por data
@app.route("/api/news", methods=["GET"])
def get_news():
    date_str = request.args.get('date') # Pega a data da query string
    if not date_str:
        return jsonify({"error": "Parâmetro 'date' é obrigatório"}), 400

    # Busca as notícias no banco de dados para a data especificada
    news_items = News.query.filter_by(date=date_str).limit(20).all() # Limita a 20 notícias

    # Converte os objetos News em dicionários para jsonify
    news_list = []
    for news in news_items:
        news_list.append({
            "id": news.id,
            "date": news.date,
            "image": news.image,
            "title": news.title,
            "summary": news.summary,
            "category": news.category
        })
    
    return jsonify(news_list)
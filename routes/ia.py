from app import app, db
from flask import request, jsonify
import os
from google import genai
from google.genai import types

@app.route("/api/generate_analysis", methods=["POST"])
def generate_analysis_api():
    client = genai.Client()
    modelo = "gemini-2.0-flash"

    data = request.get_json()
    title = data.get("title")
    summary = data.get("summary")

    if not title or not summary:
        return jsonify({"error": "Título e resumo são obrigatórios."}), 400

    prompt = f"""
    Você receberá um título e um resumo de notícia.
    Como um especialista em direito digital, forneça uma breve análise das implicações legais da notícia, 
    focando em aspectos relevantes para um escritório de advocacia:
    A análise deve ser concisa e objetiva.
    Evite utilizar markdown na sua resposta, prefira códigos html"""

    chat_config = types.GenerateContentConfig(
        system_instruction = prompt
    )

    try:
        chat = client.chats.create(
            model=modelo,
            config=chat_config,
        )
        response = chat.send_message(f"""Faça uma análise da seguinte notícia:
                                     Título: {title}
                                     Resumo: {summary}
                                     """)
        return jsonify({"analysis": response.text})
    except Exception as e:
        app.logger.error(f"Erro ao chamar a API Gemini: {e}")
        return jsonify({"error": "Ocorreu um erro ao gerar a análise jurídica."}), 500


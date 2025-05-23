#import os
#import json
#from google import genai
#from app import app
#from flask import jsonify, request
#from google.adk.agents import Agent
#from google.adk.runners import Runner
#from google.adk.sessions import InMemorySessionService
#from google.genai import types

# A chave será lida da variável de ambiente
# É CRÍTICO que esta variável de ambiente seja definida ANTES de iniciar a aplicação.
#GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Verificação básica para garantir que a chave foi carregada
#if not GOOGLE_API_KEY:
#    raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não está configurada.")

# Configura o cliente genai com a chave da variável de ambiente
#genai.configure(api_key=GOOGLE_API_KEY)
#client = genai.Client() # Não é mais necessário passar a chave diretamente se usar genai.configure()

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
#def call_agent(agent: Agent, message_text: str, file_data: bytes = None, file_mime_type: str = None) -> str:
    # Cria um serviço de sessão em memória
#    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
#    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
#    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria a lista de partes para o conteúdo da mensagem de entrada
#    parts = [types.Part(text=message_text)] # Começa com a parte de texto

    # Se dados da imagem foram fornecidos, cria uma parte para a imagem e a adiciona à lista
#    if file_data and file_mime_type:
#        image_part = types.Part(
#            inline_data={
#                "data": file_data,
#                "mime_type": file_mime_type,
#            }
#        )
#        parts.append(image_part)

    # Cria o conteúdo da mensagem de entrada
#    content = types.Content(role="user", parts=parts)

#    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
#    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
#        if event.is_final_response():
#          for part in event.content.parts:
#            if part.text is not None:
#              final_response += part.text
#              final_response += "\n"
#    return final_response

# Agentes de IA criados
#def agente_interprete_planos_alimentares(dados_entrada, file_data, file_mime_type):
#   interprete_fotos = Agent(
#        name="agente_interprete_planos_alimentares",
#        model="gemini-2.0-flash",
#        instruction="""
#        Você é um especialista em culinária e nutrição.
#        Você vai receber como informação uma breve texto explicando os dados de entrada e o foco da sua resposta.
#        Você também receberá um arquivo para analisar.
#        Siga as instruções do texto para analisar o arquivo e gerar a resposta no formato solicitado.
#        """,
#        description="Agente especialista em padronizar informações de planos alimentares"
#    )

#   analise_final = call_agent(interprete_fotos, dados_entrada, file_data=file_data, file_mime_type=file_mime_type)
#   return analise_final

# Funções de chamada dos agentes
#@app.route('/agentes_ia/getPlanoAlim', methods=['POST'])
#def getPlanoAlim():
#    if 'plano' not in request.files:
#        return jsonify({"error": "Nenhum plano foi enviada na requisição."}), 400

#    file = request.files['plano']

    # Verifica se o nome do arquivo está vazio (caso o usuário não tenha selecionado um arquivo)
#    if file.filename == '':
#        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

#    try:
        # Lê o conteúdo binário do arquivo
#        arquivo_data = file.read()
#        arquivo_mime_type = file.mimetype

        # Define as instruções de texto para o agente
#        dados_entrada = """Estou enviando um arquivo anexo de um plano alimentar.\n
#                        Analise as informações desse arquivo.
#                        Como resposta quero um texto semelhante ao exemplo abaixo:

#                        Validade do plano: de 01/05/2025 até 18/05/2025
#                        Objetivo do plano: Emagrecimento
#                        Café da manhã: 3 ovos, 2 fatias de pão e 300ml de leite
#                        Almoço: Salada de folhas verdes com frango grelhado
#                        Jantar: Sopa de legumes com tofu
#                        """

        # Chama a função agente_interprete_planos_alimentares, passando o texto E o arquivo
#        resposta_agente = agente_interprete_planos_alimentares(dados_entrada, arquivo_data, arquivo_mime_type)

#        return jsonify(resposta_agente)

#    except Exception as e:
        # Tratamento de erro básico caso algo dê errado ao ler o arquivo ou chamar o agente
#        return jsonify({"error": f"Ocorreu um erro ao processar o plano alimentar: {e}"}), 500
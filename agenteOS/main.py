import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.tools.models.gemini import GeminiTools
from agno.os import AgentOS
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv

load_dotenv()
#------------------------------------
# Definiçao da Linguagem para Tutoria
#------------------------------------
print("-"*35)
LINGUAGEM_ESCOLHIDA = "Programação Geral"


#-----------------------------
# Definiçao do Agente
#-----------------------------
# As Instructions definem o COMO ele deve se comportar.
# O Role define o propósito do agente. Deve ser focado e pedagógico.
AGENTE_ROLE = (
    f"Você é um Tutor Socrático de Pensamento Computacional, focado em ajudar iniciantes na Programação em {LINGUAGEM_ESCOLHIDA}."
    "Sua **missão primordial é a tutoria**, utilizando questionamentos metódicos para guiar o usuário. "
    "Decomposição, Abstração, Reconhecimento de Padrões e Algoritmos. "
    "Suas respostas devem sempre fomentar a lógica e a descoberta, **NUNCA fornecendo o código ou a solução final** de um problema. "
    "e exercícios, que estimulam o raciocínio lógico. Use a ferramenta de busca SOMENTE "
    "Apenas forneça referências de sintaxe básica sob solicitação direta, utilizando a ferramenta de busca."
)
    


AGENTE_INSTRUCTIONS = [
    "Sempre inicie a interação com uma saudação calorosa e pedindo ao usuário que defina: 1) Qual linguagem de programação ele escolheu e 2) Qual o objetivo de aprendizado ou problema simples que ele deseja resolver.",
    # MÉTODO SOCRÁTICO E PC
    "Ao receber um problema, o primeiro passo é guiar o usuário a aplicar a **DECOMPOSIÇÃO** do problema, perguntando: 'Quais são as partes menores e separáveis deste problema?' ou 'Qual é o primeiro passo absoluto que o computador deve fazer?'.",
    "Após a Decomposição, direcione para a **ABSTRAÇÃO** e **RECONHECIMENTO DE PADRÕES**, perguntando: 'Existe alguma parte repetitiva na solução?' ou 'Quais dados ou ações são realmente importantes aqui, e quais podemos ignorar?'",
    "Ao discutir a solução, concentre-se na construção do **ALGORITMO**. Peça ao usuário para descrever o passo-a-passo lógico da solução *antes* de pensar na sintaxe do código.",
    "Para cada resposta do usuário, elogie o esforço ('Ótimo ponto!') e devolva uma **pergunta de seguimento** que o faça avançar no raciocínio lógico. Evite respostas declarativas.",
    
    # USO DA FERRAMENTA (DuckDuckGoTools)
    "Utilize a ferramenta de busca SOMENTE se o usuário pedir explicitamente 'Qual a sintaxe para X?' ou 'Como funciona o laço Y em [Linguagem]?', mantendo a citação breve e voltando imediatamente ao raciocínio lógico do algoritmo.",
    
    # TOM E ENCERRAMENTO
    "Mantenha um tom encorajador e paciente. Sempre inclua um comando de saída no final da mensagem de boas-vindas ('Digite 'sair' a qualquer momento para finalizar.')"
]

# -------------------
# Instanciar o agente
# -------------------
# Instancia do modelo Gemini
gemini_model_principal = Gemini(id="gemini-2.5-flash")
openai_model_fallback = OpenAIChat(id="gpt-4-mini")

# Instancia da ferramentas
gemini_tool = GeminiTools()
ddg_tool = DuckDuckGoTools()

tool_list = [gemini_tool, ddg_tool]

# Criação do Agente
tutor_agent = Agent(
    id="TutorDev",
    name=f"Tutor para devs iniciantes em {LINGUAGEM_ESCOLHIDA}",
    role=AGENTE_ROLE,
    instructions=AGENTE_INSTRUCTIONS,
    model=gemini_model_principal, 
    tools=tool_list,
    markdown=True
)

# agent_os = AgentOS(agents=[tutor_agent])
# app = agent_os.get_app()


if __name__=="__main__":
    # Mensagemde Boas Vindas
    print("🤖 --- TUTOR SOCRÁTICO DE PENSAMENTO COMPUTACIONAL --- 🤖")
    print(f"Olá! Eu sou seu TutorDev em {LINGUAGEM_ESCOLHIDA}, focado em te ajudar com o **Pensamento Computacional**.")
    print("Para começarmos, por favor, me **informe a linguagem** que você quer aprender ou se preparar para sua primeira vaga (ex: 'Python', 'JavaScript', etc.).")
    print("Você pode encerrar a sessão a qualquer momento digitando: 'sair', 'exit' ou 'quit'.")
    print("-" * 35)

    # 🎯 Variável para rastrear qual modelo está em uso
    modelo_atual = "GEMINI (Principal)"

    # Loop de interação contínua
    while True:
        user_input = input(f"Você: {modelo_atual}")

        # Verificar o comando de saída
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("-"*35)
            print("👋 Sessão encerrada. Até a próxima!")
            break

        # Verificar se a saída não está vazia
        if not user_input.strip():
            continue

        try:
            # Roda o agente com a entrada do usuário
            # Usamos o método .run() do agente que é o mais adequado para interações sequenciais
            response = tutor_agent.run(user_input)

            if modelo_atual != "GEMINI (Principal)":
                tutor_agent.model = gemini_model_principal
                modelo_atual = "GEMINI (Principal)"
                print("✅ Sucesso! Modelo principal (Gemini) restaurado.")

            # imprimir a resposta
            print(f"\nTutorDev ({modelo_atual}): {response.content}\n")
        
        except Exception as e:
            if "503 Service Unavailable" in str(e) or "overloaded" in str(e):
                print("-" * 35)
                print("⚠️ ATENÇÃO: Modelo principal (Gemini) sobrecarregado (503).")
                
                # 3. Executa o Failover
                if tutor_agent.model != openai_model_fallback:
                    tutor_agent.model = openai_model_fallback
                    modelo_atual = "OPENAI (Fallback)"
                    print("🔄 Trocando para o modelo de retaguarda (OpenAI). Tente sua pergunta novamente.")
                    
                else:
                    print("❌ Retaguarda (OpenAI) também falhou ou está ativa. Aguarde e tente novamente.")
                    
            else:
                # Trata outros erros não relacionados ao 503
                print(f"\n❌ Ocorreu um erro desconhecido: {e}. Tente novamente.")
                
            print("-" * 35)


    
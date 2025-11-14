# Agente de teste Agno
from agno.agent import Agent
from agno.models.google import Gemini
from agno.os import AgentOS
from agno.tools.mcp import MCPTools
from dotenv import load_dotenv

load_dotenv()


# Instanciando o Agent da Agno
agent = Agent(
    name="Agno Agent",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")]
)

# Criar o agente
agent_os = AgentOS(agents=[agent])

# Obter o fastAPI para o agent
app = agent_os.get_app()

# Rodar o agente
if __name__ == "__main__":
    agent_os.serve("test:app", reload=True)
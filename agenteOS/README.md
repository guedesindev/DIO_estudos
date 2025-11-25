# 🤖 Agente de IA que auxilia na preparação para mercado de trabalho

Se você é iniciante em programação ou está tentando fazer a migração de área, este agente de IA é para você. Promete te ajudar no início da jornada até a conquista de tua primeira vaga de emprego na área de TI. 

A ideia é oferecer auxilio na preparação para entrevistas e com introdução ao pensamento computacional.

## 🎯 Objetivo 

Ajudar o usuário iniciante a aprender programação do zero ou então prepará-lo para entrevistas de emprego na área dev.

## 👩🏽‍💻 Como usar?

A primeira coisa é fazer o fork ou o clone do repositório. Depois de estar com o repositório no teu computador basta navegar até o diretório criado pelo prompt/terminal e proceder criar um ambiente virtual e realizar a instalação das dependências.

---
## Tecnologias
este projeto foi desenvolvido na linguagem python, na IDE vscode e com ajuda da LLM Gemini.
A tecnologia que gerencia o agente é [Agno](https://www.agno.com/). Dentro da ferramenta Agno há várias opções, para este projeto foi utilizado:
 - [!agenteOS](https://docs.agno.com/agent-os/introduction). A quantidade de opções para desenvolvimento surpreende;
 - [!Agente](https://docs.agno.com/reference/agents/agent) do Agno;
 - [!Modelo Gemini](https://docs.agno.com/reference/models/gemini);
 - [!OpenAIChat](https://docs.agno.com/reference/models/openai);
 - [!DuckDuckGo](https://docs.agno.com/integrations/toolkits/search/duckduckgo) utilizado como buscador de informações na web.

*Observação*: Dois Modelos de LLM estão sendo utilizados pensando na contingência, caso um esteja indisponível, o outro será executado automaticamente.
---

### Iniciando o ambiente virtual

**Criação do Ambiente**
```basg
    # LINUX / MAC
    python3 -m venv nome_do_ambiente

    # WINDOWS
    python -m venv nome_do_ambiente

    # Este nome_do_ambiente você escolhe, eu costumo usar '.env'
```

**Iniciar o ambiente**
```bash
    # LINUX / MAC
    source nome_do_ambiente/bin/activate

    # WINDOWS
    nome_do_ambiente/Scripts/activate
```

Agora que esta com o ambiente virtual ativado poderá instalar as dependências do projeto sem afetar o teu ambiente atual.

**Instalando as dependências do projeto**

```bash
    # Linux / MAC / WINDOWS
    pip install -r requirements.txt
```

**Agora é só executar o script**
```bash
    #LINUX / Mac
    python3 main.py

    # WINDOWS
    python main.py
```

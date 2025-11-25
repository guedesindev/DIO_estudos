# 🤖 Agente de IA que auxilia na preparação para mercado de trabalho

Se você é iniciante em programação ou está tentando fazer a migração de área, este agente de IA é para você. Promete te ajudar no início da jornada até a conquista de tua primeira vaga de emprego na área de TI. 

A ideia é oferecer auxilio na preparação para entrevistas e com introdução ao pensamento computacional.


## 🎯 Objetivo 

Ajudar o usuário iniciante a aprender programação do zero ou então prepará-lo para entrevistas de emprego na área dev.

---
## Tecnologias
Este projeto foi desenvolvido na linguagem python, na IDE vscode e com ajuda da LLM Gemini.
A tecnologia que gerencia o agente é [Agno](https://www.agno.com/). Dentro da ferramenta Agno há várias opções, para este projeto foi utilizado:
 - [agenteOS](https://docs.agno.com/agent-os/introduction). A quantidade de opções para desenvolvimento surpreende;
 - [Agente](https://docs.agno.com/reference/agents/agent) do Agno;
 - [Modelo Gemini](https://docs.agno.com/reference/models/gemini);
 - [OpenAIChat](https://docs.agno.com/reference/models/openai);
 - [DuckDuckGo](https://docs.agno.com/integrations/toolkits/search/duckduckgo) utilizado como buscador de informações na web.

*Observação*: Dois Modelos de LLM estão sendo utilizados pensando na contingência, caso um esteja indisponível, o outro será executado automaticamente.
</br>

<div style="display:flex;flex-direction:column; align-items:center">
<span>desenvolvido com:</span>

<a href="https://github.com/agno-agi/agno/tree/main">
<picture> 
      <source width=120 media="(prefers-color-scheme: dark)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-dark.svg">
      <source width=40 media="(prefers-color-scheme: light)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg">
      <img width=120 src="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg" alt="Agno">
</picture>
</a>
</div>
<br>

<div style="display:flex; justify-content:center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-DE5833?style=for-the-badge&logo=DuckDuckGo&logoColor=white)
</div>



## 👩🏽‍💻 Como usar?

A primeira coisa é fazer o fork ou o clone do repositório. Depois de estar com o repositório no teu computador basta navegar até o diretório criado pelo prompt/terminal e proceder criar um ambiente virtual e realizar a instalação das dependências.

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

**observação2**: Para você testar a aplicação precisa gerar tuas Api Keys nas plataformas [Google Gemini](https://aistudio.google.com/app/api-keys) e [OpenAiGPT](https://platform.openai.com/api-keys). É gratis a geração e uso da chave até um determinado uso, pesquise em cada LLM para mais informações.

**O que fazer com as API KEY?**
Você precisa criar um arquivo na raiz do projeto e nomeá-lo como `.env`, e adicionar as chaves: <br>
`export GOOGLE_API_KEY`="tua_chave_api_entre_aspas"<br>
`export OPENAI_API_KEY`="tua_chave_api_entre_aspas"

_Ao salvar o arquivo já pode executar o projeto._

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

😉 Obrigado por testar esta aplicação.

Agora quero saber a tua opinião: 
Da um ⭐

Se quiser contato comigo me procure em:

<div style="display:flex; align-items:center; justify-content:center">

<a diplay="inline-block" href="https://www.linkedin.com/in/fernandoguedesdev/">[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fernandoguedesdev/)</a>
<a diplay="inline-block" href="https://github.com/guedesindev">![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
</a>
<a diplay="inline-block" hfef="mailto:guedesindev@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>
</div>

Até mais 🙋🏽

<p style="text-align:left">
  <a href="#top">⬆️ Back to Top</a>
</p>
# Estudando API com fastAPI

FastAPI é um framework python bom pois é rápido, moderno e com acentuada curva de aprendizado. Quero testar isso partindo do completo zero, apenas com a ajuda do Gemini e a documentação do fastAPI e criar minha primeira API, fazendo testes no Insomnia, usando o pydantic para modelos de dados.

## Estrutura do meu aprendizado
    [ ] Configuração inicial -
        [ ] Criação do Ambiente Virtual;
        [ ] Instalação do fastapi, comando atual (28/10/2025) - pip install "fastapi[standard]"
    [ ] Estrutura báscia da API
    [ ] Modelos de dados - Usando o `Pydantic`(essencial no fastApi)
    [ ] Primeiros endpoints CRUD - Criando, lendo, atualizando e deletando dados
    [ ] Testando API com o Insomnia - Usando variáveis e dados aleatórios para testes eficientes.

### Configuração inicial

*Criando o ambiente virtual*

Para meu projeto vou dar o nome de `.env`: 
    
    ```python
        python -m venv .env. 
    ```
    

Iniciar o ambiente virutal.

    ```python
        .env/Scripts/activate.ps1
    ```

*Instalando o fastapi e suas dependências*

Atualmente, conforme a [documentação](https://fastapi.tiangolo.com/#installation) o comando a ser usado para instalar o fastapi e as dependências básicas para o desenvolvimento de uma api é:
```python
    pip install "fastapi[standard]"
```

o módulo e a versão da instalação entre aspas, e o parâmetro `[standard]`inclui automaticamente bibliotecas essenciais e padrões que precisaríamos instalar separadamente.
`fastapi[standard]`inclui: 
```
    Uvicorn: O servidor ASGI de alta performance
    pydantic: Para validação de dados
    Starlette: O framework base sobre o qual o fastAPI é construído
    E algumas dependências padrão que o fastAPI usa para um setup padrão.
```

### Vamos ao primeiro endpoint

O primeiro endpoit será o de pegar alguma informação, e como é uma tecnologia nova, vamos pegar o famoso "Hello World" com um endpoint padrão de URL "/".

Em python, o retorno de um endpoint é dado por um método sob a decoração da api executando o verbo HTTP. Neste caso o verbo HTTP inicial será o GET. Veja como fica o código.

```python

 #1. Importa o fastAPI
 from fastapi import FastAPI

 #2. Criar uma instância do FastAPI
 app = FastAPI()

 #3. Definir o endpoit de test
 # o decorador para o método do endpoint padrão é o app.get("/")
 # A função abaixo do decorador será evocada quando houver uma requisição do tipo GET para a rota "/"
 @app.get("/")
 def home():
    # O retorno é um dicionário e o fastAPI convert para JSON
    retun {"message":"Olá Mundo"}

# Para nossa aplicação, enquanto ainda não estou usando um banco de dados, vou criar uma variável global para simular esse banco de dados.
# Para uma aplicação real, usaria um banco MongoDB, SQLAlchemy ou outros

banco_de_dados_simuldado = []
```
vou salvar este arquivo com o nome `main.py`.

Agora para testar é necessário rodar o servidor para conseguir ver o resultado.

Na versão atual, conforme a [documentação fastAPI](https://fastapi.tiangolo.com/#create-it) o comando é:
```python
    fastapi dev main.py
```

quando digitar esse comando em seu terminal, deverá ver uma saída semelhante a:
```batch
  tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories: ['E:\\Estudos\\Programação\\Python\\fastapi\\api1']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [20860] using WatchFiles
      INFO   Started server process [6244]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```

Para acessar o servidor, pode abrir seu navegador e digitar: `http://127.0.0.1:8000` ou `localhost:8000`, isso quer dizer que seu servidor está rodando na porta 8000. Ou simplesmente pode segurar a tecla CTRL e clicar no endereço que está na linha linha: `INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)` do terminal e o navegador será aberto.

Agora para testar, muda o texto que está no dicionário de retorno da função `home()` assim que salvar, o servidor irá reiniciar e já aparecerá a alteração automaticamente.

## Modleos de Dados com Pydantic

*O que é Pydantic?*
É uma biblioteca de validação de dados que usa a sintaxe de anotação do tipo do Python para definir a estrutura de dados.
Vamos usar a pydantic para definir a estrutura de dados (Modelos/Schemes). Qual a vantagem? Garante que os dados que chegam à API estão no formato correto, conforme esperado na função.

Vamos criar uma lista de tarefas, para isso vamos criar um modelo de uma item da lista (To-Do List)

Para isso importamos a BaseModel da pydantic
```python
    # Importar BaseModel para criar o modelo de dados
    from pydantic import BaseModel

    # Definição do MOdelo de Dados (Schema)
    class Tarefa(BaseModel):
        id: int                   # Pydantic garante que este campo será um número inteiro
        titulo: str               # Pydantic garante que este campo será uma string
        descricao: str|None=None  # | none indica que o campo pode ter uma string ou Nulo, isto é, é um campo opcional
        concluida: bool = False   # Valor padrão como False

    banco_de_dados_simulado: list[Tarefa] = [] # A lista agora armazena objetos do tipo Tarefa
    proximo_id = 1
```
Agora a ideia é criar Endpoints para inserção de tarefas e validar os dados com o pydantic, vamos ver como funciona.

### Endpoints CRUD (Create, Read, Update, Delete)

Agora basta criar o endpoint do tipo `post` para que uma nova tarefa seja inserida no banco de dados simulado e o fastAPI ira se encarregar de fazer as validações.

```python
    # endpoint para criação de nova tarefa
    @app.post("/tarefa/")
    def criar_tarefa(tarefa:Tarefa):
        # Uma rotina para gerenciamento do id, porque não estamos usando um banco de dados real, senão o próprio banco faria esse gerenciamento
        global proximo_id

        tarefa.id = proximo_id
        proximo_id += 1

        banco_de_dados_simulado.append(tarefa)

        return tarefa
```

### Testando com Insomnia e Variáveis Aleatórias
# ETL com Python


## Proposição
Como cientistas de dados nos fora passada uma lista de ids de clientes do banco para que fossem criadas mensagens automáticas via IA e enviadas para o e-mail do cliente.

## Minha Composição

Havia uma API criada anteriormente (2023) que serviria como fonte de dados dos clientes, pesquisa de seus nomes, com base na lista de ids passadas. Entretanto, hoje a API não está disponível, assim sendo, criei a minha própria fonte de dados de clientes.

### Minha Lista de Clientes

Para criar a lista de clientes e não ter de ficar alimentando tal lista manualmente, eu criei um script python que gera automaticamente uma relação de 1000 clientes, gerando nomes automáticos com sobrenomes, cpfs fictícios, e-mail igualmente fictícios, números de agência e conta, categorias de contas, cartões. 

Estou disponibilizando neste repositório o código do script. Para executá-lo basta seguir as instruções abaixo de execução do projeto.

### Fluxo de ETL

Aqui criei arquivos separados para Extrat, Transform e Load. Para dar soporte a estes processos criei arquivos auxiliares como messages.py, gerador.py.
O desafio consiste em ler o arquivo `ids.csv`, criar uma lista de ids a partir deste arquivo, buscar os clientes na base: `clientes.csv`, e ao localizar seu id, verificar a categoria de sua conta, cartão de crédito que possui e limite, esses dados são utilizados para categorizar as mensagens que estão no arquivo message.py. Em posse dos ids e dos dados dos clientes, as mensagens são geradas e um arquivo `news.csv` é gerado. Deste arquivo, o conteúdo está pronto para ser envidado.

### Dificuldades

Como já havia dito, a API não estava mais disponível, então tive de criar uma nova abordagem para o exercício.

Não usei a API da OpenAi por que não está mais disponível a versão gratuita para testes, e não quis investir recursos neste exercício, por isso criei meu prórpio gerador de mensagens de marketing. 

## Como executar os scripts?

Seguir os passos:

**Criar o ambiente virtual**
```python
    # WINDOWS
    python -m venv venv

    #LINUX/MAC
    python3 -m venv venv
```

**Ativar o ambiente virtual**

```python
    # WINDOWS
    venv/Scripts/activate

    # LINUX/MAC
    source venv/bin/activate
```
 **Instalar as dependências**

 ```python
    # Há o arquivo com todas as dependências para rodar esse projeto então basta fazer
    # WINDOWS / LINUX / MAC
    pip install -r requirements.txt
 ```

 Agora pode executar os scripts
 **Gerador de Clientes**
 ```python
     # WINDOWS
     python gerador.py

     # LINUX/MAC
     python3 gerador.py
 ```

 Você verá o surgimento do arquivo `usuarios.csv`

 Agora para ver o Pipeline do ETL basta executar o arquivo main.py
 ```python
     # WINDOWS
     python main.py

     # LINUX/MAC
     python3 main.py
 ```

 E pronto, o arquivo `news.csv` é criado e pronto para enviar as mensagens para os clientes.

 Espero que tenham gostado da minha abordagem.

from fastapi import Depends, FastAPI, HTTPException, Header, Response, status

from pydantic import BaseModel

app = FastAPI(title="ToDo List")

banco_de_dados_simulado = []
# ==========================================================
# NOVO: Injeção de dependência (dependência de autenticação)
# ==========================================================

# Esta função de dependência é rodada pelo FastAPI antes de rodar a rota
def verificar_api_key(x_api_key: str = Header(..., description="Chave de API necessária para acessar este recurso.")):
    """Verifica se a chave de API é a esperada"""

    # Simulação: A chave correta é: "CHAVE_SECRETA_123"
    if x_api_key != "CHAVE_SECRETA_123":
        # se falhar levanta exceção HTTPException
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Chave de API inválida."
        )
    
    # Se for bem-sucedido, retorna um valor (ou nada)
    return True


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message":"Olá mundo do fastapi!"}


# ===================================
# Aplicando a dependência a uma rota
# ===================================

# --- READ (ler todas as tarefas) ---
@app.get('/tarefas/', 
         dependencies=[Depends(verificar_api_key)]) # NOVO: A rota AGORA DEPENDE da função de verificação de chave.
def listar_tarefas():
    # Esta função é executada apenas se 'verificar_api_key' retornar True
    return banco_de_dados_simulado

# --- READ (ler uma tarefa pelo ID, sem verificação de dependência)
@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id:int):
    for tarefa in banco_de_dados_simulado:
        if tarefa.id == tarefa_id:
            return tarefa
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# --- DELETE (somente consegue deletar uma tarefa usuário que possui chave da API
@app.delete('/tarefas/{tarefa_id}', status_code=status.HTTP_404_NOT_FOUND, dependencies=[Depends(verificar_api_key)])
def deletar_tarefe(tarefa_id):
    banco_de_dados_simulado.pop(tarefa_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)






# 📒 O que preciso aprender/pesquisar:

## CORE
[ ] Como criar API REST com FastAPI

[ ] Como conectar FastAPI a banco de dados

[ ] Como fazer relacionamentos 1:N em SQL

## FERRAMENTAS
[ ] SQLAlchemy (ORM)

[ ] Pydantic (validação)

[ ] Uvicorn (servidor)

## CONCEITOS
[ ] CRUD operativas

[ ] Foreign Keys

[ ] Schema vs Models


# 🔎 Onde Pesquisar

## Tier 1: Documnetação Oficial
1. FastAPI: https://fastapi.tiangolo.com/
   → Procure: "Tutorial - User Guide" → "SQL Databases"
   
2. SQLAlchemy: https://docs.sqlalchemy.org/
   → Procure: "ORM Quick Start"
   
3. Pydantic: https://docs.pydantic.dev/
   → Procure: "Models"

## Tier 2: Tutoriais específcos
1. YouTube: "FastAPI SQLite tutorial"

2. Real Python: "FastAPI + Databases"

3. Dev.to / Medium: "Building REST API with FastAPI"

## Tier 3: Comunidade
1. Stack Overflow (problemas específicos)

2. GitHub Issues (bugs conhecidos)

3. Reddit r/FastAPI

## Tier 4: Como estrutura suas pesquisas no Google
❌ Ruim: "como fazer api python"

✅ Bom: "FastAPI SQLAlchemy SQLite tutorial"

✅ Melhor: "FastAPI one to many relationship SQLAlchemy example"

**Fórmula**

`[Tecnologia] + [Conceito Específico] + [Caso de Uso] + "tutorial" ou "example"`

---

# 📐 PARTE 3: PLANEJAMENTO ANTES DE CODAR

🗺️ Mapa Mental do Projeto
```map
API de Usuários
│
├── 📊 Dados (O QUÊ?)
│   ├── Users (id, name, email)
│   ├── Accounts (id, user_id, number, agency, balance, limit)
│   └── Cards (id, user_id, number, validate, cod)
│
├── 🔄 Funcionalidades (PARA QUÊ?)
│   ├── POST /users (criar usuário)
│   ├── GET /users/{id} (buscar usuário)
│   ├── POST /accounts (criar conta)
│   └── GET /users/{id}/accounts (listar contas do usuário)
│
└── 🏗️ Arquitetura (COMO?)
    ├── FastAPI (rotas)
    ├── SQLAlchemy (ORM)
    ├── Pydantic (validação)
    └── SQLite (persistência)
```


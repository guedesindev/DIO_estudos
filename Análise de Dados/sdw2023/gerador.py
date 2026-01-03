import random

# Listas para gerar usuários aleatórios
nomes = [
    "Ádila",
    "João",
    "Maria",
    "Carlos",
    "Ana",
    "Kátia" "Ricardo",
    "Beatriz",
    "Fernando",
    "Juliana",
    "Lucas",
    "Patrícia",
    "Roberto",
]
sobrenomes = [
    "Alves",
    "Silva",
    "Oliveira",
    "Souza",
    "Costa",
    "Santos",
    "Pereira",
    "Ferreira",
    "Almeida",
    "Nascimento",
    "Guedes",
]
tipos_conta = ["Corrente", "Poupanca", "Universitária"]
tipos_cartao = ["Débito", "Crédito Platinum", "Crédito Black", "Crédito Infinite"]


def gerar_cpf():
    return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"


with open("usuarios2.csv", "a", encoding="utf-8") as f:
    # Cabeçalho
    f.write(
        "id_usuario;nome;cpf;email;tipo_conta;agencia;numero_conta;limite_especial;tipo_cartao;final_cartao;limite_cartao\n"
    )

    for i in range(1, 1001):
        nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        email = f"{nome_completo.lower().replace(' ', '.')}@email.com"
        cpf = gerar_cpf()
        t_conta = random.choice(tipos_conta)
        agencia = f"{random.randint(1, 10):04d}"
        n_conta = f"{random.randint(10000, 99999)}-{random.randint(0, 9)}"
        limite_esp = round(random.uniform(0, 5000), 2) if t_conta == "Corrente" else 0.0
        t_cartao = random.choice(tipos_cartao)
        final_c = random.randint(1000, 9999)
        limite_c = (
            round(random.uniform(1000, 50000), 2) if "Crédito" in t_cartao else 0.0
        )

        linha = f"{i};{nome_completo};{cpf};{email};{t_conta};{agencia};{n_conta};{limite_esp};{t_cartao};{final_c};{limite_c}\n"
        f.write(linha)

print("Arquivo 'usuarios.csv' com 1000 usuários gerado com sucesso!")

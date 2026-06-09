from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"],
)

# --- Lógica de Persistência ---
ARQUIVO_CONTAS = "contas.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_CONTAS):
        with open(ARQUIVO_CONTAS, "r") as f:
            return json.load(f)
    return {
        "111": {"nome": "Zack", "saldo": 1000.0},
        "222": {"nome": "Maria", "saldo": 250.0}
    }

def salvar_dados(contas):
    with open(ARQUIVO_CONTAS, "w") as f:
        json.dump(contas, f, indent=4)

# Inicializa as contas carregando do arquivo (ou criando o padrão)
contas = carregar_dados()

# --- Rotas ---
@app.get("/")
def visualizar_contas():
    return contas

@app.post("/transferir")
def realizar_transferencia(dados: dict):
    origem = dados['origem']
    destino = dados['destino']
    valor = float(dados['valor'])

    if origem not in contas or destino not in contas:
        return {"erro": "Conta de origem ou destino inválida"}

    if contas[origem]['saldo'] < valor:
        return {"erro": "Saldo insuficiente"}

    contas[origem]['saldo'] -= valor
    contas[destino]['saldo'] += valor
    
    # Salva no arquivo após a alteração
    salvar_dados(contas)

    return {"mensagem": "Transferência realizada com sucesso"}
# cliente_gerente.py - Cliente em modo texto para gerentes
import requests

BASE_URL = 'http://127.0.0.1:5000'

print("=== Cliente Gerente ===")

menu = [
    "\nOpções:",
    "1 - Ver todas as tarefas",
    "2 - Ver tarefas pendentes",
    "3 - Ver funcionários sem tarefas pendentes",
    "0 - Sair"
]

loop = True
while loop:
    for linha in menu:
        print(linha)

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        try:
            resp = requests.get(f"{BASE_URL}/relatorio/tarefas")
            tarefas = resp.json()
            print("\nTodas as tarefas:")
            for t in tarefas:
                print(f"ID: {t[0]} | Descrição: {t[1]} | Status: {t[2]}")
        except Exception as e:
            print("Erro ao obter tarefas:", e)

    elif escolha == '2':
        try:
            resp = requests.get(f"{BASE_URL}/relatorio/pendentes")
            pendentes = resp.json()
            print("\nTarefas pendentes:")
            for t in pendentes:
                print(f"ID: {t[0]} | Descrição: {t[1]}")
        except Exception as e:
            print("Erro ao obter pendentes:", e)

    elif escolha == '3':
        try:
            resp = requests.get(f"{BASE_URL}/relatorio/funcionarios_livres")
            livres = resp.json()
            print("\nFuncionários sem tarefas pendentes:")
            for f in livres:
                print(f"ID: {f[0]} | Nome: {f[1]}")
        except Exception as e:
            print("Erro ao obter funcionários livres:", e)

    elif escolha == '0':
        loop = False
    else:
        print("Opção inválida.")

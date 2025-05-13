# cliente_funcionario.py - Cliente em modo texto para funcionários
import requests
import sys

BASE_URL = 'http://127.0.0.1:5000'

print("=== Cliente Funcionário ===")

# Obter ID do funcionário via argumento ou padrão
if len(sys.argv) > 1:
    id_func = sys.argv[1]
else:
    id_func = input("Digite o ID do funcionário: ") or '1'

menu_opcoes = [
    "\nOpções:",
    "1 - Ver tarefas",
    "2 - Concluir tarefa",
    "0 - Sair"
]

loop = True
while loop:
    for linha in menu_opcoes:
        print(linha)

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        try:
            resp = requests.get(f"{BASE_URL}/tarefas/{id_func}")
            tarefas = resp.json()
            if tarefas:
                print("\nTarefas:")
                for t in tarefas:
                    print(f"ID: {t[0]} | Descrição: {t[1]} | Status: {t[2]}")
            else:
                print("Nenhuma tarefa encontrada.")
        except Exception as e:
            print("Erro ao buscar tarefas:", e)

    elif escolha == '2':
        tarefa_id = input("Digite o ID da tarefa que deseja concluir: ")
        try:
            resp = requests.post(f"{BASE_URL}/concluir_tarefa", json={"tarefa_id": tarefa_id})
            print(resp.json())
        except Exception as e:
            print("Erro ao concluir tarefa:", e)

    elif escolha == '0':
        loop = False
    else:
        print("Opção inválida.")

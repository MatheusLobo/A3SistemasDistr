# cliente_supervisor.py - Cliente em modo texto para supervisores
import requests

BASE_URL = 'http://127.0.0.1:5000'

print("=== Cliente Supervisor ===")
supervisor_id = input("Digite o ID do supervisor (ex: 2): ") or "2"

menu = [
    "\nOpções:",
    "1 - Cadastrar nova tarefa",
    "2 - Ver tarefas de um funcionário",
    "0 - Sair"
]

loop = True
while loop:
    for linha in menu:
        print(linha)

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        descricao = input("Descrição da nova tarefa: ")
        funcionario_id = input("ID do funcionário para a tarefa: ")
        try:
            resp = requests.post(f"{BASE_URL}/cadastrar_tarefa", json={
                "descricao": descricao,
                "funcionario_id": funcionario_id,
                "supervisor_id": supervisor_id
            })
            print(resp.json())
        except Exception as e:
            print("Erro ao cadastrar tarefa:", e)

    elif escolha == '2':
        funcionario_id = input("Digite o ID do funcionário: ")
        try:
            resp = requests.get(f"{BASE_URL}/tarefas_funcionario/{funcionario_id}")
            tarefas = resp.json()
            if tarefas:
                print("\nTarefas:")
                for t in tarefas:
                    print(f"ID: {t[0]} | Descrição: {t[1]} | Status: {t[2]}")
            else:
                print("Nenhuma tarefa encontrada para este funcionário.")
        except Exception as e:
            print("Erro ao buscar tarefas:", e)

    elif escolha == '0':
        loop = False
    else:
        print("Opção inválida.")

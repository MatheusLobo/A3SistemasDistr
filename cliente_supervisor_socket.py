import socket

HOST = 'localhost'
PORT = 5001

print("=== Cliente Supervisor ===")
id_supervisor = input("Digite o ID do supervisor: ").strip()

def enviar_comando(msg):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(msg.encode())
            return s.recv(4096).decode()
    except Exception as e:
        return f"Erro ao se conectar ao servidor: {e}"

menu = [
    "\nOpções:",
    "1 - Cadastrar nova tarefa",
    "2 - Ver tarefas de um funcionário",
    "0 - Sair"
]

while True:
    print("\n".join(menu))
    escolha = input("Escolha uma opção: ").strip()

    if escolha == '1':
        desc = input("Descrição da tarefa: ").strip()
        id_func = input("ID do funcionário: ").strip()
        comando = f"CADASTRAR_TAREFA {desc}|{id_func}|{id_supervisor}"
        resposta = enviar_comando(comando)
        print(resposta)

    elif escolha == '2':
        id_func = input("ID do funcionário: ").strip()
        resposta = enviar_comando(f"GET_TAREFAS {id_func}")
        print(resposta)

    elif escolha == '0':
        break

    else:
        print("Opção inválida.")

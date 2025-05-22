import socket

HOST = 'localhost'
PORT = 5001

print("=== Cliente Funcionário ===")
id_func = input("Digite o ID do funcionário: ")

def enviar_comando(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg.encode())
        return s.recv(4096).decode()

menu = [
    "\nOpções:",
    "1 - Ver tarefas",
    "2 - Concluir tarefa",
    "0 - Sair"
]

while True:
    print("\n".join(menu))
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        resposta = enviar_comando(f"GET_TAREFAS {id_func}")
        print("\n" + resposta)

    elif escolha == '2':
        id_tarefa = input("Digite o ID da tarefa a concluir: ")
        resposta = enviar_comando(f"CONCLUIR_TAREFA {id_tarefa}")
        print(resposta)

    elif escolha == '0':
        break

    else:
        print("Opção inválida.")

import socket

HOST = 'localhost'
PORT = 5001

def enviar_comando(msg):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(msg.encode())
            return s.recv(4096).decode()
    except Exception as e:
        return f"Erro ao conectar: {e}"

print("=== Cliente Gerente ===")

menu = [
    "\nOpções:",
    "1 - Ver todas as tarefas",
    "2 - Ver tarefas pendentes",
    "3 - Ver funcionários sem tarefas pendentes",
    "0 - Sair"
]

while True:
    print("\n".join(menu))
    escolha = input("Escolha uma opção: ").strip()

    if escolha == '1':
        print(enviar_comando("RELATORIO_TODAS"))

    elif escolha == '2':
        print(enviar_comando("RELATORIO_PENDENTES"))

    elif escolha == '3':
        print(enviar_comando("RELATORIO_LIVRES"))

    elif escolha == '0':
        break

    else:
        print("Opção inválida.")

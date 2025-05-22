import socket
import sqlite3

HOST = 'localhost'
PORT = 5001
DB_NAME = 'database.db'

def executar_sql(query, args=(), fetch=True):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(query, args)
    resultado = cur.fetchall() if fetch else None
    if not fetch:
        conn.commit()
    conn.close()
    return resultado

def tratar_comando(msg):
    try:
        if msg.startswith("GET_TAREFAS"):
            _, id_func = msg.strip().split()
            tarefas = executar_sql("SELECT id, descricao, status FROM tarefas WHERE funcionario_id = ?", (id_func,))
            if tarefas:
                return "\n".join([f"{t[0]} - {t[1]} - {t[2]}" for t in tarefas])
            return "Nenhuma tarefa encontrada."

        elif msg.startswith("CONCLUIR_TAREFA"):
            _, id_tarefa = msg.strip().split()
            executar_sql("UPDATE tarefas SET status = 'concluida' WHERE id = ?", (id_tarefa,), fetch=False)
            return "Tarefa concluída com sucesso."

        elif msg.startswith("CADASTRAR_TAREFA"):
            try:
                dados = msg.strip().split(" ", 1)[1]
                if "|" not in dados or dados.count("|") != 2:
                    return "Erro: formato inválido. Use descricao|funcionario_id|supervisor_id"
                descricao, func_id, sup_id = dados.split("|")
                executar_sql(
                    "INSERT INTO tarefas (descricao, status, funcionario_id, supervisor_id) VALUES (?, 'pendente', ?, ?)",
                    (descricao.strip(), func_id.strip(), sup_id.strip()),
                    fetch=False
                )
                return "Tarefa cadastrada com sucesso."
            except Exception as e:
                return f"Erro ao cadastrar tarefa: {e}"

        elif msg.strip() == "RELATORIO_TODAS":
            tarefas = executar_sql("SELECT id, descricao, status FROM tarefas")
            return "\n".join([f"{t[0]} - {t[1]} - {t[2]}" for t in tarefas]) or "Sem tarefas."

        elif msg.strip() == "RELATORIO_PENDENTES":
            pendentes = executar_sql("SELECT id, descricao FROM tarefas WHERE status = 'pendente'")
            return "\n".join([f"{t[0]} - {t[1]}" for t in pendentes]) or "Sem tarefas pendentes."

        elif msg.strip() == "RELATORIO_LIVRES":
            livres = executar_sql("""
                SELECT id, nome FROM usuarios 
                WHERE tipo = 'funcionario' AND id NOT IN (
                    SELECT funcionario_id FROM tarefas WHERE status = 'pendente'
                )
            """)
            return "\n".join([f"{f[0]} - {f[1]}" for f in livres]) or "Nenhum funcionário livre."

    except Exception as e:
        return f"Erro ao processar comando: {e}"

    return "Comando desconhecido."

if __name__ == '__main__':
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(5)
            print(f"Servidor escutando em {HOST}:{PORT}...")

            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"\n[+] Conectado com {addr}")
                    data = conn.recv(4096)
                    if not data:
                        continue
                    mensagem = data.decode().strip()
                    print(f"[>] Comando recebido: {mensagem}")
                    resposta = tratar_comando(mensagem)
                    conn.sendall(resposta.encode())
    except OSError as e:
        print(f"Erro ao iniciar o servidor socket: {e}")

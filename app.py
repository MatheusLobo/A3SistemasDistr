# app.py - Servidor Flask
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'database.db'

# Função para acessar o banco de dados
def query_db(query, args=(), one=False, commit=False):
    if not os.path.exists(DB_NAME):
        return [] if not one else None
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(query, args)
    if commit:
        con.commit()
        con.close()
        return
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

# Funcionario - Listar tarefas
@app.route('/tarefas/<int:id_funcionario>', methods=['GET'])
def listar_tarefas(id_funcionario):
    tarefas = query_db("SELECT id, descricao, status FROM tarefas WHERE funcionario_id = ?", (id_funcionario,))
    return jsonify(tarefas)

# Funcionario - Concluir tarefa
@app.route('/concluir_tarefa', methods=['POST'])
def concluir_tarefa():
    dados = request.get_json()
    tarefa_id = dados.get('tarefa_id')
    query_db("UPDATE tarefas SET status = 'concluida' WHERE id = ?", (tarefa_id,), commit=True)
    return jsonify({'status': 'ok'})

# Supervisor - Cadastrar tarefa
@app.route('/cadastrar_tarefa', methods=['POST'])
def cadastrar_tarefa():
    dados = request.get_json()
    desc = dados.get('descricao')
    func_id = dados.get('funcionario_id')
    sup_id = dados.get('supervisor_id')
    query_db("INSERT INTO tarefas (descricao, status, funcionario_id, supervisor_id) VALUES (?, 'pendente', ?, ?)",
             (desc, func_id, sup_id), commit=True)
    return jsonify({'status': 'tarefa criada'})

# Supervisor - Listar tarefas de funcionario
@app.route('/tarefas_funcionario/<int:id_funcionario>', methods=['GET'])
def tarefas_func(id_funcionario):
    tarefas = query_db("SELECT id, descricao, status FROM tarefas WHERE funcionario_id = ?", (id_funcionario,))
    return jsonify(tarefas)

# Gerente - Relatorio de todas as tarefas
@app.route('/relatorio/tarefas', methods=['GET'])
def relatorio_tarefas():
    tarefas = query_db("SELECT id, descricao, status FROM tarefas")
    return jsonify(tarefas)

# Gerente - Relatorio de tarefas pendentes
@app.route('/relatorio/pendentes', methods=['GET'])
def relatorio_pendentes():
    pendentes = query_db("SELECT id, descricao FROM tarefas WHERE status = 'pendente'")
    return jsonify(pendentes)

# Gerente - Funcionarios sem tarefas pendentes
@app.route('/relatorio/funcionarios_livres', methods=['GET'])
def funcionarios_livres():
    livres = query_db("SELECT id, nome FROM usuarios WHERE tipo = 'funcionario' AND id NOT IN (SELECT funcionario_id FROM tarefas WHERE status = 'pendente')")
    return jsonify(livres)

if __name__ == '__main__':
    if not os.path.exists(DB_NAME):
        print(f"Erro: banco de dados '{DB_NAME}' não encontrado. Rode 'init_db.py' para criar o banco.")
    else:
        app.run(debug=False, use_reloader=False)

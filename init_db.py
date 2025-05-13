# init_db.py - Cria e popula o banco de dados SQLite
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Criar tabelas
c.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('funcionario', 'supervisor', 'gerente')) NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    status TEXT CHECK(status IN ('pendente', 'concluida')) NOT NULL,
    funcionario_id INTEGER,
    supervisor_id INTEGER,
    FOREIGN KEY (funcionario_id) REFERENCES usuarios(id),
    FOREIGN KEY (supervisor_id) REFERENCES usuarios(id)
)
''')

# Inserir dados de exemplo
c.execute("INSERT INTO usuarios (nome, tipo) VALUES ('Marcos', 'funcionario')")
c.execute("INSERT INTO usuarios (nome, tipo) VALUES ('Matheus', 'supervisor')")
c.execute("INSERT INTO usuarios (nome, tipo) VALUES ('Willian', 'gerente')")

conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso.")

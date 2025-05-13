# Projeto - Sistema de Acompanhamento de Tarefas (Cliente-Servidor)

## Descrição
Este projeto é uma aplicação cliente-servidor desenvolvida para a disciplina de Sistemas Distribuídos e Mobile. Ele permite o acompanhamento de tarefas por diferentes perfis de usuários: Funcionário, Supervisor e Gerente.

## Equipe
- Matheus Lobo de Souza Martins 1272312529
- [------]
- [------]
- [------]

## Tecnologias Utilizadas
- Linguagem: Python 3
- Framework: Flask
- Banco de Dados: SQLite
- Biblioteca HTTP para os clientes: `requests`

## Estrutura do Projeto
```
├── app.py                  # Servidor Flask
├── init_db.py              # Script para criar e popular o banco
├── cliente_funcionario.py  # Cliente do funcionário
├── cliente_supervisor.py   # Cliente do supervisor
├── cliente_gerente.py      # Cliente do gerente
├── database.db             # Banco de dados SQLite
├── README.md               # Este arquivo
```

## Instruções para Execução

### 1. Instalar dependências
```bash
pip install flask requests
```

### 2. Criar o banco de dados
```bash
python init_db.py
```

### 3. Iniciar o servidor
```bash
python app.py
```

### 4. Executar os clientes
- Funcionário:
  ```bash
  python cliente_funcionario.py 1
  ```
- Supervisor:
  ```bash
  python cliente_supervisor.py
  ```
- Gerente:
  ```bash
  python cliente_gerente.py
  ```

## Justificativa da Abordagem de Comunicação
Foi utilizada a abordagem de **API REST via Flask**, por ser simples, direta e eficaz para o modelo cliente-servidor proposto. Essa escolha permite fácil manutenção, escalabilidade e testes com ferramentas padrão como `curl` ou Postman.

##  Funcionalidades por Perfil
- **Funcionário**:
  - Ver tarefas atribuídas
  - Concluir tarefas

- **Supervisor**:
  - Cadastrar tarefas para funcionários
  - Ver tarefas atribuídas a um funcionário

- **Gerente**:
  - Relatório de todas as tarefas
  - Relatório de tarefas pendentes
  - Lista de funcionários sem tarefas pendentes

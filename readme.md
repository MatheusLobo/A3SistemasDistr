# Projeto - Sistema de Acompanhamento de Tarefas (Cliente-Servidor via Socket)

## Descrição
Este projeto é uma aplicação cliente-servidor desenvolvida para a disciplina de Sistemas Distribuídos e Mobile. Ele permite o acompanhamento de tarefas por diferentes perfis de usuários: Funcionário, Supervisor e Gerente, usando **comunicação via sockets TCP**.

## Equipe
- Matheus Lobo de Souza Martins 1272312529
- William Bitencourt de Castro 12723115263
- Paullo Victor de Carvalho Marques 12723117914
- Vinicius Rian de Jesus Moreira 1272311431
- Marcos Leones Leite Souza 1272312642
-

## Tecnologias Utilizadas
- Linguagem: Python 3
- Banco de Dados: SQLite
- Comunicação entre cliente-servidor: Socket TCP (módulo `socket`)
- Interface: Terminal (modo texto)

## Estrutura do Projeto
```
├── servidor_socket.py            # Servidor baseado em sockets TCP
├── cliente_funcionario_socket.py # Cliente terminal para funcionários
├── cliente_supervisor_socket.py  # Cliente terminal para supervisores
├── cliente_gerente_socket.py     # Cliente terminal para gerentes
├── init_db.py                    # Script para criar e popular o banco
├── database.db                   # Banco de dados SQLite
├── README.md                     # Este arquivo
```

## Instruções para Execução

### 1. Instalar Python 3 e bibliotecas padrão
Não há dependências externas — apenas `socket` e `sqlite3`, que já vêm com o Python.

### 2. Criar o banco de dados
Execute o script para criar e popular o banco:

```bash
python init_db.py
```

### 3. Iniciar o servidor de socket
Execute o servidor que ficará escutando os clientes:

```bash
python servidor_socket.py
```

### 4. Executar os clientes (cada um em um terminal separado)

- Funcionário:
  ```bash
  python cliente_funcionario_socket.py
  ```

- Supervisor:
  ```bash
  python cliente_supervisor_socket.py
  ```

- Gerente:
  ```bash
  python cliente_gerente_socket.py
  ```

## Justificativa da Abordagem de Comunicação
Inicialmente planejamos implementar a comunicação utilizando API REST com Flask, o que é indicado para aplicações web mais estruturadas e escaláveis. No entanto, optamos por utilizar sockets TCP para fins educacionais, pois isso nos proporciona maior controle sobre a comunicação entre cliente e servidor, além de permitir o aprofundamento em conceitos fundamentais de redes e protocolos. Essa abordagem também se alinha bem aos objetivos da disciplina de Sistemas Distribuídos, focando na simulação de interações de baixo nível entre nós da rede

## Funcionalidades por Perfil

- **Funcionário**:
  - Ver tarefas atribuídas
  - Concluir tarefas

- **Supervisor**:
  - Cadastrar tarefas para funcionários
  - Ver tarefas de um funcionário específico

- **Gerente**:
  - Ver todas as tarefas
  - Ver apenas tarefas pendentes
  - Ver funcionários sem tarefas pendentes
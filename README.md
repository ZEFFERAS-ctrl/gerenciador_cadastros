# Gerenciador de Cadastros

Aplicação desktop para gerenciamento de cadastros de clientes, desenvolvida em Python com CustomTkinter e MariaDB.

## ✨ Funcionalidades

- ➕ Cadastrar clientes
- ❌ Excluir cadastros pelo CPF
- 📋 Listar clientes cadastrados
- 🔍 Pesquisar clientes pelo nome
- 💾 Armazenar os dados em um banco de dados MariaDB local

## 🛠️ Tecnologias

- Python
- CustomTkinter
- MariaDB
- Biblioteca `mariadb` para conexão com o banco de dados

## 📋 Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3
- MariaDB Server
- As bibliotecas Python utilizadas pelo projeto

Instale as dependências com:

```bash
pip install customtkinter mariadb
```

## 🗄️ Configuração do banco de dados

O programa utiliza um banco de dados MariaDB local. **Antes de executar o projeto, é necessário configurar o arquivo `lib.py` de acordo com o seu banco de dados local.**

No início do `lib.py`, procure pela configuração de conexão:

```python
conexao = mariadb.connect(
    user="root",
    password="1234",
    host="localhost",
    port=3306,
    database="omnimind"
)
```

Modifique os valores de `user`, `password`, `host`, `port` e `database` conforme a configuração do seu MariaDB.

### ⚠️ Importante

O banco de dados e a tabela utilizados pelo programa precisam existir no MariaDB antes da execução. O código atualmente utiliza a tabela `clientes` com os campos:

- `nome`
- `cpf`
- `email`
- `telefone`

Se o seu banco de dados tiver outro nome, outro usuário, outra senha ou estiver configurado em uma porta diferente, **é obrigatório alterar a conexão no `lib.py`**.

## ▶️ Executando o projeto

Depois de configurar o MariaDB e ajustar o `lib.py`, execute o arquivo principal do projeto com Python.

Exemplo:

```bash
python main.py
```

> Substitua `main.py` pelo nome correto do arquivo principal, caso seja diferente no seu projeto.

## 📁 Estrutura

```text
Gerenciador de Cadastros/
├── lib.py
├── main.py
└── ...
```

O arquivo `lib.py` contém as funções e interfaces responsáveis pelo cadastro, exclusão, listagem e pesquisa dos clientes, além da conexão com o banco de dados.

## 🔒 Observação sobre segurança

As credenciais do banco de dados estão atualmente diretamente no código do `lib.py`. Em ambientes reais, recomenda-se utilizar variáveis de ambiente ou outro método seguro para armazenar senhas e informações de conexão.

## 👨‍💻 Autor

ZEFFERAS-ctrl

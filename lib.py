import customtkinter as ctk
import mariadb

# Conexão com o banco
try:
    conexao = mariadb.connect(
        user="root",
        password="1234",
        host="localhost",
        port=3306,
        database="omnimind"
    )
    sql = conexao.cursor()

except mariadb.Error as e:
    print(f"Erro de conexão: {e}")
    exit(1)


def pagina_cadastro():
    def cadastrar():
        try:
            usuario = campo_usuario.get()
            cpf = campo_cpf.get()
            email = campo_email.get()
            telefone = campo_telefone.get()

            sql.execute('INSERT INTO clientes (nome, cpf, email, telefone) VALUES (?, ?, ?, ?)', (usuario, cpf, email, telefone))
            conexao.commit()
            feedback.configure(text='✅ Cadastrado com Sucesso!', text_color='green')

        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            feedback.configure(text='❌ Erro no Cadastro!', text_color='red')

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    app = ctk.CTk()
    app.title('Cadastro de Cliente')
    app.geometry('400x500')
    app.resizable(False, False)

    titulo = ctk.CTkLabel(app, text='Cadastrar Cliente', font=('Arial Black', 24), text_color='cyan')
    titulo.pack(pady=20)

    usuario = ctk.CTkLabel(app, text='Nome:', font=('Arial', 14))
    usuario.pack(pady=5)

    campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite o Nome', width=300, corner_radius=10)
    campo_usuario.pack(pady=10)

    cpf = ctk.CTkLabel(app, text='CPF:', font=('Arial', 14))
    cpf.pack(pady=5)

    campo_cpf = ctk.CTkEntry(app, placeholder_text='Digite o CPF', width=300, corner_radius=10)
    campo_cpf.pack(pady=10)

    email = ctk.CTkLabel(app, text='Email:', font=('Arial', 14))
    email.pack(pady=5)

    campo_email = ctk.CTkEntry(app, placeholder_text='Seu melhor Email', width=300, corner_radius=10)
    campo_email.pack(pady=10)

    telefone = ctk.CTkLabel(app, text='Telefone:', font=('Arial', 14))
    telefone.pack(pady=5)

    campo_telefone = ctk.CTkEntry(app, placeholder_text='seu numero de telefone', width=300, corner_radius=10)
    campo_telefone.pack(pady=10)

    cadastro = ctk.CTkButton(
        app, text='➕ Cadastrar', command=cadastrar,
        fg_color='green', hover_color='darkgreen', corner_radius=20,
        width=250, height=50, font=('Arial', 16)
    )
    cadastro.pack(pady=20)

    feedback = ctk.CTkLabel(app, text='', font=('Arial', 14))
    feedback.pack(pady=10)

    app.mainloop()
    conexao.close()


def pagina_delete():
    def n1_delete():
        try:
            apagar_cadastro = int(campo_del.get())
            sql.execute('DELETE FROM clientes WHERE cpf = ?', (apagar_cadastro,))
            conexao.commit()
            feedback.configure(text='✅ Cadastro Deletado!', text_color='green')
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            feedback.configure(text='❌ Erro ao Deletar!', text_color='red')

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    app = ctk.CTk()
    app.title('Deletar Cadastro')
    app.geometry('400x330')
    app.resizable(False, False)

    titulo = ctk.CTkLabel(app, text='Excluir Cliente', font=('Arial Black', 24), text_color='cyan')
    titulo.pack(pady=20)

    instrucoes = ctk.CTkLabel(app, text='Informe o CPF do cliente para excluir:', font=('Arial', 14))
    instrucoes.pack(pady=10)

    campo_del = ctk.CTkEntry(app, placeholder_text='Digite o CPF', width=300, corner_radius=10)
    campo_del.pack(pady=10)

    button_del = ctk.CTkButton(
        app, text='❌ Deletar', command=n1_delete,
        fg_color='red', hover_color='darkred', corner_radius=20,
        width=250, height=50, font=('Arial', 16)
    )
    button_del.pack(pady=20)

    feedback = ctk.CTkLabel(app, text='', font=('Arial', 14))
    feedback.pack(pady=20)

    app.mainloop()
    conexao.close()


def pagina_lista():
    def listar():
        try:
            sql.execute('SELECT nome, cpf, email, telefone FROM clientes')
            registros = sql.fetchall()

            texto.delete("1.0", "end")
            for nome, cpf, email, telefone in registros:
                texto.insert("end", f"👤 Nome: {nome}\n🆔 CPF: {cpf}\n📧 Email: {email}\n📱 Phone: {telefone}\n\n")

        except Exception as e:
            print(f"Erro ao listar: {e}")
            texto.delete("1.0", "end")
            texto.insert("end", "❌ Erro ao buscar cadastros.")

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    app = ctk.CTk()
    app.title('Lista de Cadastros')
    app.geometry('450x570')
    app.resizable(False, False)

    titulo = ctk.CTkLabel(app, text='Usuários Cadastrados', font=('Arial Black', 24), text_color='cyan')
    titulo.pack(pady=20)

    texto = ctk.CTkTextbox(app, width=400, height=400, corner_radius=15, font=('Arial', 14))
    texto.pack(pady=10)

    botao_listar = ctk.CTkButton(
        app, text='🔄 Atualizar Lista', command=listar,
        fg_color='blue', hover_color='navy', corner_radius=20,
        width=250, height=50, font=('Arial', 16)
    )
    botao_listar.pack(pady=20)

    app.mainloop()
    conexao.close()


def pagina_pesquisa():
    def pesquisa():
        try:
            nome_digitado = campo_pesquisa.get().strip()

            if not nome_digitado:
                texto.delete("1.0", "end")
                texto.insert("end", "⚠️ Digite um nome para pesquisar.\n")
                return

            sql.execute(
                "SELECT nome, cpf, email, telefone FROM clientes WHERE nome LIKE ?",
                (f"%{nome_digitado}%",)
            )

            resultados = sql.fetchall()

            texto.delete("1.0", "end")

            if resultados:
                for nome, cpf, email, telefone in resultados:
                    texto.insert(
                        "end",
                        f"👤 Nome: {nome}\n"
                        f"🆔 CPF: {cpf}\n"
                        f"📧 Email: {email}\n"
                        f"📱 Telefone: {telefone}\n\n"
                    )
            else:
                texto.insert("end", "❌ Nenhum cadastro encontrado com esse nome.")

        except Exception as e:
            texto.delete("1.0", "end")
            texto.insert("end", f"❌ Erro ao buscar cadastros: {str(e)}")

    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')

    app = ctk.CTk()
    app.title('Pesquisar Cadastro')
    app.geometry('450x380')
    app.resizable(False, False)

    titulo = ctk.CTkLabel(
        app,
        text='Pesquisar Cadastros',
        font=('Arial Black', 24),
        text_color='cyan'
    )
    titulo.pack(pady=20)

    instrucoes = ctk.CTkLabel(
        app,
        text='Digite o nome do cliente:',
        font=('Arial', 14)
    )
    instrucoes.pack(pady=5)

    campo_pesquisa = ctk.CTkEntry(
        app,
        placeholder_text='Digite o nome',
        width=300,
        corner_radius=10
    )
    campo_pesquisa.pack(pady=10)

    botao_pesquisa = ctk.CTkButton(
        app,
        text='🔍 Pesquisar',
        command=pesquisa,
        fg_color='blue',
        hover_color='navy',
        corner_radius=20,
        width=200,
        height=50,
        font=('Arial', 16)
    )
    botao_pesquisa.pack(pady=10)

    texto = ctk.CTkTextbox(
        app,
        width=400,
        height=100,
        corner_radius=15,
        font=('Arial', 16)
    )
    texto.pack(pady=10)

    app.mainloop()
    conexao.close()

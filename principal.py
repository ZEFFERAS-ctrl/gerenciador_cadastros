import customtkinter as ctk
import lib

def cadastrar():
    lib.pagina_cadastro()

def deletar():
    lib.pagina_delete()

def listar():
    lib.pagina_lista()

def pesquisar():
    lib.pagina_pesquisa()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("OmniMind")
app.geometry("900x500")
app.resizable(False, False)

# ===== Barra lateral =====
sidebar = ctk.CTkFrame(app, width=220, corner_radius=0)
sidebar.pack(side="left", fill="y")

titulo = ctk.CTkLabel(
    sidebar,
    text="📂 OmniMind",
    font=("Arial Black", 24),
    text_color="cyan"
)
titulo.pack(pady=(30, 5))

subtitulo = ctk.CTkLabel(
    sidebar,
    text="Gerenciador\nDe Cadastros",
    font=("Arial", 14),
    justify="center"
)
subtitulo.pack(pady=(0, 30))

ctk.CTkButton(
    sidebar,
    text="➕ Adicionar",
    command=cadastrar,
    width=160,
    height=45,
    corner_radius=12,
    fg_color="#404040",
    hover_color="#505050"
).pack(pady=8)

ctk.CTkButton(
    sidebar,
    text="📋 Listar",
    command=listar,
    width=160,
    height=45,
    corner_radius=12,
    fg_color="#404040",
    hover_color="#505050"
).pack(pady=8)

ctk.CTkButton(
    sidebar,
    text="🔎 Pesquisar",
    command=pesquisar,
    width=160,
    height=45,
    corner_radius=12,
    fg_color="#404040",
    hover_color="#505050"
).pack(pady=8)

ctk.CTkButton(
    sidebar,
    text="❌ Excluir",
    command=deletar,
    fg_color="#b91c1c",
    hover_color="#991b1b",
    width=165,
    height=45,
    corner_radius=12
).pack(pady=8)

# ===== Área principal =====
main = ctk.CTkFrame(app, fg_color="transparent")
main.pack(expand=True, fill="both")

ctk.CTkLabel(
    main,
    text="Bem-vindo ao OmniMind",
    font=("Arial Black", 30)
).pack(pady=(70, 10))

ctk.CTkLabel(
    main,
    text="Sistema de gerenciamento de clientes\nutilizando Python e MariaDB.",
    font=("Arial", 18),
    text_color="gray"
).pack()

info = ctk.CTkTextbox(main, width=500, height=180)
info.pack(pady=40)
info.insert(
    "0.0",
    "📌 Escolha uma opção no menu lateral.\n\n"
    "➕ Adicionar um cliente\n"
    "📋 Listar todos os clientes\n"
    "🔎 Pesquisar por nome\n"
    "❌ Excluir um cadastro"
)
info.configure(state="disabled")

app.mainloop()

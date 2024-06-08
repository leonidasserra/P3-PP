import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from Biblio import *

class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Biblioteca")
        self.biblioteca = Biblioteca()

        self.create_widgets()

    def create_widgets(self):
        # Criar os widgets
        self.tab_control = ttk.Notebook(self.master)

        # Tabs
        self.tab_cadastrar = ttk.Frame(self.tab_control)
        self.tab_exibir = ttk.Frame(self.tab_control)
        self.tab_localizar = ttk.Frame(self.tab_control)
        self.tab_excluir = ttk.Frame(self.tab_control)
        self.tab_alterar = ttk.Frame(self.tab_control)
        self.tab_emprestar = ttk.Frame(self.tab_control)
        self.tab_reservar = ttk.Frame(self.tab_control)
        self.tab_encerrar = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_cadastrar, text="Cadastrar Livro")
        self.tab_control.add(self.tab_exibir, text="Exibir Livros")
        self.tab_control.add(self.tab_localizar, text="Localizar Livro")
        self.tab_control.add(self.tab_excluir, text="Excluir Livro")
        self.tab_control.add(self.tab_alterar, text="Alterar Livro")
        self.tab_control.add(self.tab_emprestar, text="Emprestar Livro")
        self.tab_control.add(self.tab_reservar, text="Reservar Livro")
        self.tab_control.add(self.tab_encerrar, text="Encerrar Empréstimo")

        self.tab_control.pack(expand=1, fill="both")

        # Tab Cadastrar Livro
        self.label_nome = tk.Label(self.tab_cadastrar, text="Nome do Livro:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.tab_cadastrar)
        self.entry_nome.pack()

        self.label_codigo = tk.Label(self.tab_cadastrar, text="Código do Livro:")
        self.label_codigo.pack()
        self.entry_codigo = tk.Entry(self.tab_cadastrar)
        self.entry_codigo.pack()

        self.label_editora = tk.Label(self.tab_cadastrar, text="Editora:")
        self.label_editora.pack()
        self.entry_editora = tk.Entry(self.tab_cadastrar)
        self.entry_editora.pack()

        self.label_ano = tk.Label(self.tab_cadastrar, text="Ano:")
        self.label_ano.pack()
        self.entry_ano = tk.Entry(self.tab_cadastrar)
        self.entry_ano.pack()

        self.label_valor_pago = tk.Label(self.tab_cadastrar, text="Valor Pago:")
        self.label_valor_pago.pack()
        self.entry_valor_pago = tk.Entry(self.tab_cadastrar)
        self.entry_valor_pago.pack()

        self.button_cadastrar = tk.Button(self.tab_cadastrar, text="Cadastrar Livro", command=self.cadastrar_livro)
        self.button_cadastrar.pack()

        # Tab Exibir Livros
        self.button_exibir = tk.Button(self.tab_exibir, text="Exibir Livros", command=self.exibir_livros)
        self.button_exibir.pack()
        self.text_exibir = tk.Text(self.tab_exibir)
        self.text_exibir.pack()

        # Tab Localizar Livro
        self.label_localizar_codigo = tk.Label(self.tab_localizar, text="Código do Livro:")
        self.label_localizar_codigo.pack()
        self.entry_localizar_codigo = tk.Entry(self.tab_localizar)
        self.entry_localizar_codigo.pack()

        self.button_localizar = tk.Button(self.tab_localizar, text="Localizar Livro", command=self.localizar_livro)
        self.button_localizar.pack()
        self.text_localizar = tk.Text(self.tab_localizar)
        self.text_localizar.pack()

        # Tab Excluir Livro
        self.label_excluir_codigo = tk.Label(self.tab_excluir, text="Código do Livro:")
        self.label_excluir_codigo.pack()
        self.entry_excluir_codigo = tk.Entry(self.tab_excluir)
        self.entry_excluir_codigo.pack()

        self.button_excluir = tk.Button(self.tab_excluir, text="Excluir Livro", command=self.excluir_livro)
        self.button_excluir.pack()

        # Tab Alterar Livro
        self.label_alterar_codigo = tk.Label(self.tab_alterar, text="Código do Livro:")
        self.label_alterar_codigo.pack()
        self.entry_alterar_codigo = tk.Entry(self.tab_alterar)
        self.entry_alterar_codigo.pack()

        self.label_alterar_nome = tk.Label(self.tab_alterar, text="Novo Nome:")
        self.label_alterar_nome.pack()
        self.entry_alterar_nome = tk.Entry(self.tab_alterar)
        self.entry_alterar_nome.pack()

        self.label_alterar_editora = tk.Label(self.tab_alterar, text="Nova Editora:")
        self.label_alterar_editora.pack()
        self.entry_alterar_editora = tk.Entry(self.tab_alterar)
        self.entry_alterar_editora.pack()

        self.label_alterar_ano = tk.Label(self.tab_alterar, text="Novo Ano:")
        self.label_alterar_ano.pack()
        self.entry_alterar_ano = tk.Entry(self.tab_alterar)
        self.entry_alterar_ano.pack()

        self.label_alterar_valor_pago = tk.Label(self.tab_alterar, text="Novo Valor Pago:")
        self.label_alterar_valor_pago.pack()
        self.entry_alterar_valor_pago = tk.Entry(self.tab_alterar)
        self.entry_alterar_valor_pago.pack()


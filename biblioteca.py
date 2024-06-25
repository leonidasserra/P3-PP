import json
import os
from livro import Livro

db_file = os.path.join(os.path.dirname(__file__), 'database.json')

class Biblioteca:
    def __init__(self):
        self.load_data()

    def load_data(self):
        if os.path.exists(db_file):
            with open(db_file, 'r') as f:
                self.info_livros = {k: Livro.from_dict(v) for k, v in json.load(f).items()}
        else:
            self.info_livros = {}

    def save_data(self):
        with open(db_file, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.info_livros.items()}, f)

    def cadastrar_livro(self, codigo, livro):
        self.info_livros[codigo] = livro
        self.save_data()

    def exibir_livros(self):
        return self.info_livros

    def localizar_livro(self, codigo):
        return self.info_livros.get(codigo)

    def excluir_livro(self, codigo):
        if codigo in self.info_livros:
            del self.info_livros[codigo]
            self.save_data()

    def alterar_livro(self, codigo, updated_data):
        if codigo in self.info_livros:
            livro = self.info_livros[codigo]
            livro.nome = updated_data.get('nome', livro.nome)
            livro.editora = updated_data.get('editora', livro.editora)
            livro.ano = updated_data.get('ano', livro.ano)
            livro.valorpago = updated_data.get('valor_pago', livro.valorpago)
            self.save_data()

    def emprestar_livro(self, codigo, emprestador):
        livro = self.info_livros.get(codigo)
        if livro:
            if livro.emprestimo == '' and livro.reserva is None:
                livro.emprestimo = emprestador
                self.save_data()
                return True
            elif livro.emprestimo == '' and emprestador == livro.reserva:
                livro.emprestimo = emprestador
                livro.reserva = None
                self.save_data()
                return True
        return False

    def reservar_livro(self, codigo, nome_reservante):
        livro = self.info_livros.get(codigo)
        if livro and livro.reserva is None:
            livro.reserva = nome_reservante
            self.save_data()
            return True
        return False

    def encerrar_emprestimo(self, codigo):
        livro = self.info_livros.get(codigo)
        if livro and livro.emprestimo != '':
            livro.emprestimo = ''
            self.save_data()
            return True
        return False

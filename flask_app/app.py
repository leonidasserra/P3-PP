from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
db_file = 'database.json'

if not os.path.exists(db_file):
    with open(db_file, 'w') as f:
        json.dump({}, f)

class Livro:
    def __init__(self, nome, editora, ano, valor_pago, emprestimo='', reserva=None):
        self.nome = nome
        self.editora = editora
        self.ano = ano
        self.valor_pago = valor_pago
        self.emprestimo = emprestimo
        self.reserva = reserva

    def to_dict(self):
        return {
            'nome': self.nome,
            'editora': self.editora,
            'ano': self.ano,
            'valor_pago': self.valor_pago,
            'emprestimo': self.emprestimo,
            'reserva': self.reserva
        }

class Biblioteca:
    def __init__(self):
        self.load_data()

    def load_data(self):
        with open(db_file, 'r') as f:
            self.info_livros = json.load(f)

    def save_data(self):
        with open(db_file, 'w') as f:
            json.dump(self.info_livros, f)

    def cadastrar_livro(self, codigo, livro):
        self.info_livros[codigo] = livro.to_dict()
        self.save_data()

    def exibir_livros(self):
        return self.info_livros

    def localizar_livro(self, codigo):
        return self.info_livros.get(codigo)

    def excluir_livro(self, codigo):
        if codigo in self.info_livros:
            del self.info_livros[codigo]
            self.save_data()
            return True
        return False

    def alterar_livro(self, codigo, updated_data):
        if codigo in self.info_livros:
            self.info_livros[codigo].update(updated_data)
            self.save_data()
            return True
        return False

    def emprestar_livro(self, codigo, emprestador):
        livro = self.info_livros.get(codigo)
        if livro:
            if livro['emprestimo'] == '' and livro['reserva'] is None:
                livro['emprestimo'] = emprestador
                self.save_data()
                return True
            elif livro['emprestimo'] == '' and emprestador == livro['reserva']:
                livro['emprestimo'] = emprestador
                livro['reserva'] = None
                self.save_data()
                return True
        return False

    def reservar_livro(self, codigo, nome_reservante):
        livro = self.info_livros.get(codigo)
        if livro and livro['reserva'] is None:
            livro['reserva'] = nome_reservante
            self.save_data()
            return True
        return False

    def encerrar_emprestimo(self, codigo):
        livro = self.info_livros.get(codigo)
        if livro and livro['emprestimo'] != '':
            livro['emprestimo'] = ''
            self.save_data()
            return True
        return False

biblioteca = Biblioteca()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        editora = request.form['editora']
        ano = request.form['ano']
        valor_pago = request.form['valor_pago']
        livro = Livro(nome, editora, ano, valor_pago)
        biblioteca.cadastrar_livro(codigo, livro)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/view')
def view_books():
    books = biblioteca.exibir_livros()
    return render_template('view_books.html', books=books)

@app.route('/edit/<codigo>', methods=['GET', 'POST'])
def edit_book(codigo):
    livro = biblioteca.localizar_livro(codigo)
    if not livro:
        return 'Book not found', 404
    if request.method == 'POST':
        updated_data = {
            'nome': request.form['nome'],
            'editora': request.form['editora'],
            'ano': request.form['ano'],
            'valor_pago': request.form['valor_pago']
        }
        biblioteca.alterar_livro(codigo, updated_data)
        return redirect(url_for('view_books'))
    return render_template('edit_book.html', livro=livro, codigo=codigo)

@app.route('/delete/<codigo>')
def delete_book(codigo):
    biblioteca.excluir_livro(codigo)
    return redirect(url_for('view_books'))

@app.route('/reserve/<codigo>', methods=['GET', 'POST'])
def reserve_book(codigo):
    if request.method == 'POST':
        nome_reservante = request.form['nome_reservante']
        biblioteca.reservar_livro(codigo, nome_reservante)
        return redirect(url_for('view_books'))
    livro = biblioteca.localizar_livro(codigo)
    if not livro:
        return 'Book not found', 404
    return render_template('reserve_book.html', livro=livro, codigo=codigo)

@app.route('/loan/<codigo>', methods=['GET', 'POST'])
def loan_book(codigo):
    if request.method == 'POST':
        emprestador = request.form['emprestador']
        biblioteca.emprestar_livro(codigo, emprestador)
        return redirect(url_for('view_books'))
    livro = biblioteca.localizar_livro(codigo)
    if not livro:
        return 'Book not found', 404
    return render_template('loan_book.html', livro=livro, codigo=codigo)

@app.route('/return/<codigo>')
def return_book(codigo):
    biblioteca.encerrar_emprestimo(codigo)
    return redirect(url_for('view_books'))

if __name__ == '__main__':
    app.run(debug=True)

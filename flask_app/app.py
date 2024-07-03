from flask import Flask, render_template, request, redirect, url_for
import sys
import os

# Adiciona o diretório pai ao caminho do sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from biblioteca import Biblioteca
from livro import Livro

app = Flask(__name__)

# Instanciando a biblioteca
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


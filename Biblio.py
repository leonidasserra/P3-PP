class Livro:
    def __init__(self, nome, editora, ano, valor_pago, emprestimo='', reserva=None):
        self.nome = nome
        self.editora = editora
        self.ano = ano
        self.valorpago = valor_pago
        self.emprestimo = emprestimo
        self.reserva = reserva

    def __str__(self):
        return f"Nome: {self.nome}\nEditora: {self.editora}\nAno: {self.ano}\nValor Pago: {self.valorpago}\nEmprestimo: {self.emprestimo}\n"


class Biblioteca:
    def __init__(self):
        self.info_livros = {}

    def cadastrar_livro(self, codigo, livro):
        self.info_livros[codigo] = livro

    def exibir_livros(self):
        for id_livro, livro in self.info_livros.items():
            print(f'Código:{id_livro} {livro}')

    def localizar_livro(self, codigo):
        livro = self.info_livros.get(codigo)
        if livro:
            print(livro)
        else:
            print('Livro não encontrado.')

    def excluir_livro(self, codigo):
        if codigo in self.info_livros:
            print('EXCLUINDO LIVRO...')
            del self.info_livros[codigo]
        else:
            print('Livro não encontrado.')

    def alterar_livro(self, codigo):
        livro = self.info_livros.get(codigo)
        if livro:
            print('Editar informações do livro:')
            livro.nome = input(f'Nome atual: {livro.nome}. Novo nome: ')
            livro.editora = input(f'Editora atual: {livro.editora}. Nova editora: ')
            livro.ano = int(input(f'Ano atual: {livro.ano}. Novo ano: '))
            livro.valorpago = float(input(f'Valor Pago atual: {livro.valorpago}. Novo valor pago: '))
            print('Informações do livro editadas com sucesso!')
        else:
            print('Livro não encontrado.')

    def emprestar_livro(self, codigo, emprestador):
        livro = self.info_livros.get(codigo)
        if livro:
            if livro.emprestimo == '' and livro.reserva is None:
                print(f'{livro.nome} está sendo emprestado para você, {emprestador}... ')
                livro.emprestimo = emprestador
            elif livro.emprestimo == '' and emprestador == livro.reserva:
                print(f'Conforme reserva, o livro {livro.nome} está sendo emprestado para você, {emprestador}...')
                livro.emprestimo = emprestador
                livro.reserva = None
            elif livro.emprestimo == '' and livro.reserva is not None:
                print('O LIVRO JÁ ESTÁ RESERVADO PARA OUTRO')
            else:
                print('LIVRO JÁ ESTÁ EMPRESTADO')
        else:
            print('Livro não encontrado.')

    def reservar_livro(self, codigo, nome_reservante):
        livro = self.info_livros.get(codigo)
        if livro:
            if livro.reserva is None:
                print(f'{livro.nome} está sendo reservado para você, {nome_reservante}... ')
                livro.reserva = nome_reservante
            else:
                print('LIVRO JÁ RESERVADO')
        else:
            print('Livro não encontrado.')

    def encerrar_emprestimo(self, codigo):
        livro = self.info_livros.get(codigo)
        if livro:
            if livro.emprestimo != '':
                print(f'O empréstimo do livro {livro.nome} foi encerrado.')
                livro.emprestimo = ''
            else:
                print('O livro não está emprestado no momento.')
        else:
            print('Livro não encontrado.')



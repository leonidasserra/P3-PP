class Livro:
    def __init__(self, nome, editora, ano, valor_pago, emprestimo='', reserva=None):
        self.nome = nome
        self.editora = editora
        self.ano = ano
        self.valorpago = valor_pago
        self.emprestimo = emprestimo
        self.reserva = reserva

    def to_dict(self):
        return {
            'nome': self.nome,
            'editora': self.editora,
            'ano': self.ano,
            'valor_pago': self.valorpago,
            'emprestimo': self.emprestimo,
            'reserva': self.reserva
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nome'], data['editora'], data['ano'], data['valor_pago'], data['emprestimo'], data['reserva'])

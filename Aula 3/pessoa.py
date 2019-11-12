class Pessoa:
    nome = ''
    sobrenome = ''
    data_nascimento = ''
    email = ''
    senha = ''
    def cadastrar_pessoa(self):
        self.nome = input ('Digite seu nome: ')
        self.sobrenome = input('Digite seu sobrenome: ')
        self.data_nascimento = input ('Digite a sua data de nascimento: ')
        self.email = input ('Digite seu e-mail: ')
        self.senha = input ('Digite sua senha: ')
        return (f'Nome: {self.nome}, sobrenome: {self.sobrenome}, data de nascimento: {self.data_nascimento}, e-mail {self.email} e  senha: {self.senha}')
        
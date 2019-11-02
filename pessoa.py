class Pessoa:
    nome = 'pescador de rã'
    def cadastrar_pessoa(self):
        nome = input ('Digite seu nome: ')
        sobrenome = input('Digite seu sobrenome: ')
        data_nascimento = input ('Digite a sua data de nascimento: ')
        email = input ('Digite seu e-mail: ')
        senha = input ('Digite sua senha: ')
        return (f'Nome: {nome}, sobrenome: {sobrenome}, data de nascimento: {data_nascimento}, e-mail {email} e  senha: {senha}')
        
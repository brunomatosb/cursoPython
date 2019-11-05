class Endereco:
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''
    def cadastrar_endereco(self):
        self.logradouro = input ('Digite o logradouro: ')
        self.numero = input('Digite o número: ')
        self.complemento = input ('Digite o complemento: ')
        self.bairro = input ('Digite seu bairro: ')
        self.cidade = input ('Digite sua cidade: ')
        self.cep = input ('Digite seu CEP:')
        return (f'Logradouro: {self.logradouro}, numero: {self.numero}, complemento: {self.complemento}, bairro {self.bairro}, cidade: {self.cidade} e CEP: {self.cep}')
        
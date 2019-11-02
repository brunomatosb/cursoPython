def cadastrar_endereco():
    logradouro = input ('Digite o logradouro: ')
    numero = input('Digite o número: ')
    complemento = input ('Digite o complemento: ')
    bairro = input ('Digite seu bairro: ')
    cidade = input ('Digite sua cidade: ')
    cep = input ('Digite seu CEP:')
    return (f'Logradouro: {logradouro}, numero: {numero}, complemento: {complemento}, bairro {bairro}, cidade: {cidade} e CEP: {cep}')
    
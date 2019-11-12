from pessoa import Pessoa
from endereco import Endereco

print ('--'*30)
print ('--'*30)

pessoa = Pessoa()
endereco = Endereco()
print (pessoa.cadastrar_pessoa())
print (endereco.cadastrar_endereco())


print ('--'*30)
print(pessoa.nome)
print(endereco.logradouro)
print ('--'*30)



#print (f'Nome: {nome}, sobrenome: {sobrenome}, data de nascimento: {data_nascimento}, e-mail {email} e  senha: {senha}.')

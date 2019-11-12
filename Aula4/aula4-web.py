from flask import Flask, render_template, request

nome_pagina = "Ambev"
app = Flask (__name__)

@app.route ('/')
def inicio ():
    lista_cervejas = []
    with open ('Aula4/cervejas.txt', 'r') as arquivo: #o 'r' serve para abrir o arquivo
        for l in arquivo:
            vetor = l.split (';')
            lista_cervejas.append(vetor)
    return render_template ('index.html',nome = nome_pagina, lista = lista_cervejas)

@app.route ('/cadastrar')# me leva para o a pagina cadastrar carro
def cadastrar():
    return render_template ('cadastrar.html',nome = nome_pagina)

@app.route ('/salvar')
def salvar ():
    nome = request.args ["nome"]
    tipo = request.args ["tipo"]
    teor = request.args ["teor"]
    with open ('Aula4/cervejas.txt', 'a') as arq:
        arq.write (f'{nome}; {tipo};{teor}\n')
    return 'salvo ' + str(nome)

app.run (debug=True)

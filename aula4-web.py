from flask import Flask, render_template, request

nome_pagina = "Ambev"
app = Flask (__name__)

@app.route ('/')
def inicio ():
    return render_template ('index.html',nome = nome_pagina)

@app.route ('/cadastrar')
def cadastrar():
    return render_template ('cadastrar.html',nome = nome_pagina)

@app.route ('/salvar')
def salvar ():
    nome = request.args ["nome"]
    tipo = request.args ["tipo"]
    teor = request.args ["teor"]
    with open ('cervejas.txt', 'a') as arq:
        arq.write (f'{nome}; {tipo};{teor}')
    return 'salvo ' + str(nome)

app.run (debug=True)

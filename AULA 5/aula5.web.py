from flask import Flask, render_template, request
from carro import Carro

nome_pagina = "Carros"
app = Flask (__name__)

@app.route ('/')
def inicio ():
    lista_carros = []
    with open ('Aula5.carros.txt', 'r') as arquivo:
        for c in arquivo:
            cl = c.strip().split (';')
            carro = Carro (cl)
    return render_template ('home.html')
  

@app.route ('/cadastrar_carro')
def cadastrar():
    return render_template ('cadastrar_carro.html')

@app.route ('/salvar')
def salvar():
    marca = request.args ['marca']
    modelo = request.args ['modelo']
    categoria = request.args ['categoria']
    ano = request.args ['ano']

    carro = Carro(marca, modelo, categoria, ano)
    with open('Aula5/carros.txt','a') as arquivo:
        arquivo.write(f'{carro.marca}; {carro.modelo}; {carro.categoria}; {carro.ano}\n')
    return 'salvo'

app.run (debug=True)

from flask import Flask

app =  Flask(__name__)

@app.route('/')
def inicio():
    return '<h1> Pagina Principalssss </h1>'

@app.route('/cerveja')
def cerveja():
    return '<h1> Cervejas </h1>'

app.run()
from flask import Flask,render_template
from aluno import Aluno
from avaliacao import Avaliacao

aluno1 = Aluno('Bruno','Bastos', 'BB', '123' )
aluno2 = Aluno( 'Pedro','seila','PS','12345')

avaliacao1 = Avaliacao ('14/04/1992', 'matematica', '10')
avaliacao2 = Avaliacao ('08/09/1990', 'portugues', '08')


app = Flask(__name__)

nome_pagina = 'Banda Calipso'
lista = [aluno1, aluno2]
lista2 = [avaliacao1,avaliacao2]

@app.route('/')
def inicio ():
    return render_template ('home.html', nome=nome_pagina, lista=lista)

@app.route ('/contato')
def contato ():
    return render_template ('contato.html', nome=nome_pagina, lista_avaliacao = lista2)

app.run(debug=True)
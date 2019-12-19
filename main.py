from flask import Flask, render_template, request, redirect, session, flash
from crud import BancoDeDados


app = Flask(__name__)

Banco = BancoDeDados()

@app.route('/login') 
def index():
	Banco.criacao()
	# titulo = e o titulo no inicio da pagina 
	return render_template('login.html',titulo='Casa Centro')
@app.route('/index')
def cliente():
	
	nome = "lucas"
	return render_template('index.html', nome = nome)
@app.route('/estatistica')
def teste():
	return render_template('estatistica.html')
	
if __name__ == '__main__':
	#debug='True' serve para atualizar sem reiniciar o servidor
	app.run(debug='True')
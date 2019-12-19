from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)


@app.route('/')
def index():
	# titulo = e o titulo no inicio da pagina 
	return render_template('index.html',titulo='Casa Centro')
@app.route('/cliente')
def cliente():
	return render_template('cliente.html')
	
if __name__ == '__main__':
	#debug='True' serve para atualizar sem reiniciar o servidor
	app.run(debug='True')
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'alura'


class Jogo():
	def __init__(self, nome, categoria, console):
		self.nome = nome
		self.categoria = categoria
		self.console = console

titulo = 'titulo-teste'

jogo_1 = Jogo('Gustavo', 'ana', 'foi')
jogo_2 = Jogo('Gustavo2', 'ana2', 'foi2')
lista = [jogo_1, jogo_2]

#--------------------------------------
@app.route('/')
def index():
	return render_template('lista.html', titulo=titulo, jogos=lista )


@app.route('/novo')
def novo():
	return render_template('novo.html', titulo='Cria um novo jogo')


@app.route('/criar',methods=['POST',])
def criar():
	nome = request.form['nome']
	categoria = request.form['categoria']
	console = request.form['console']
	jogo_n = Jogo(nome, categoria, console)
	lista.append(jogo_n)
	return redirect('/')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/autenticar',methods=['POST',])
def autenticar():
	if 'mestra' == request.form['senha']:
		flash(request.form['nome'] + ' logou com sucesso!')
		session['usuario_logado'] = request.form['nome']
		return redirect('/')
	else:
		flash('Usuario não logado!')
		return redirect('/login')

#--------------------------------------
if __name__ == '__main__':
	# app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
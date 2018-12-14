from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm, conn, engine, session

from app.models.forms import LoginForm, CadForm
import app.models.tables as tables
from sqlalchemy import func
from sqlalchemy.sql import select, insert, and_, or_, not_

from app.controllers.functions import pesquisa_primeiros



@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

@app.route('/Lojas/')
@app.route('/Lojas/<lojaBuscada>')
def Lojas(lojaBuscada=None):
	if lojaBuscada:
		s = select([tables.PRODUTO.nome]).where\
			(and_(tables.Loja.codloja == tables.CONTEM.loja,
				  and_( tables.CONTEM.produto == tables.PRODUTO.cod_produto,
						tables.Loja.nomeloja == lojaBuscada)))
		t = select([tables.Loja.codloja, tables.Loja.nomeloja, tables.Loja.telefone, tables.Loja.site]).where(tables.Loja.nomeloja == lojaBuscada)
		result = conn.execute(t)
		for row in result:
			print(row.site)
		return render_template('produtos.html', dadosLoja=conn.execute(t), dadosProd=conn.execute(s))

	else:
		s = select([tables.Loja.codloja, tables.Loja.nomeloja, tables.Loja.telefone, tables.Loja.site]).limit(15)
		return render_template('lojas.html', result=conn.execute(s))



@lm.user_loader
def load_user(id):
	return tables.Usuario.query.filter_by(codpessoa=id).first()

@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form and form.validate_on_submit():
		user = tables.Usuario.query.filter_by(email=form.email.data).first()
		if user:
			if user.senha == form.senha.data:
				login_user(user)
				flash("Você logou com sucesso.")
				return redirect(url_for("index"))
			else:
				flash("Sua senha está incorreta.")
		else:
			flash("Usuário inválido.")

	return render_template('login.html', form=form)



@app.route("/logout")
def logout():
	logout_user()
	flash("Logged out.")
	return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
	form = CadForm()
	if form.validate_on_submit():
		if form.senha.data == form.confirmasenha.data:
			if not form.assinante.data:
				s = select([tables.Usuario]).where(tables.Usuario.email==form.email.data).limit(1)
				result = conn.execute(s)

				is_unique = True
				for row in result:
					is_unique = False
					break

				if not is_unique:
					flash("Esse usuário já está registrado.")
				else:
					stmt = insert(tables.Usuario).values(
						nome=form.nome.data,
						telefonefixo = form.telefonefixo.data,
					 	telefonecelular = form.celular.data,
					 	email=form.email.data,
					 	senha=form.senha.data
					)
					conn.execute(stmt)
					flash("Você foi registrado com sucesso! Faça seu login!")
					return redirect(url_for('login'))

			else:
				s = select([tables.Assinante]).where(tables.Assinante.email==form.email.data).limit(1)
				result = conn.execute(s)
				is_unique = True
				for row in result:
					is_unique = False
					break

				if not is_unique:
					flash("Esse usuário já está cadastrado como assinante.")
				else:
					"""
					stmt = insert(tables.Assinante).values(
						codpessoa=99,
						nome=form.nome.data,
						telefonefixo = form.telefonefixo.data,
						telefonecelular = form.celular.data,
						email=form.email.data,
						senha=form.senha.data
					)
					conn.execute(stmt)
					"""
					session.execute(func.insere_assinante(form.nome.data,form.telefonefixo.data,form.celular.data,form.email.data,form.senha.data))
					session.commit()

					flash("Assinante registrado com sucesso!")
					return redirect(url_for('login'))

		else:
			flash("As senhas não batem.")



	return render_template('register.html', form=form)


#!/usr/bin/python3
import os
from app import app
from flask import render_template,redirect,url_for,request,session
from jinja2 import Environment
from flask_wtf.csrf import CSRFProtect
import emoji

jinja = Environment()
csrf = CSRFProtect(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, '../')

@app.route('/')
def index():
	home = "Halaman Utama"
	return render_template('index.html')

@app.route('/inputnama',methods=['GET','POST'])
def inputnama():
	if request.method == 'POST':
		user = request.form.get("nama","")
		return redirect(url_for("nama",nama=user))

@app.route('/nama',methods=['GET','POST'])
def nama():
		if request.method == 'GET':
			user = request.args.get("nama","")
			output = jinja.from_string(user).render()
			if user:
				sapa = "Salam kenal ya kak "
				emot = emoji.emojize(":thumbs_up:")
				return render_template('nama.html',title='Hacker Name',sapa=sapa,nama=output,emot=emot)
			else:
				emot = emoji.emojize(":thumbs_down:")
				sapa = ""
				return render_template('nama.html',title='Hacker Name',sapa=sapa,nama=output,emot=emot)



@app.route('/inputsearch',methods=['GET','POST'])
def inputsearch():
	if request.method == 'POST':
		q = request.form.get("q","")
		return redirect(url_for("search",q=q))

@app.route('/search',methods=['GET','POST'])
def search():
	if request.method == 'GET':
		q = request.args.get("q","")
		# o = jinja.from_string(q).render()
		return render_template('sqlerror.html',title='SQL error (You have an error in your SQL syntax',q=q)
		# if q:
		# 	return render_template('sqlerror.html',title='Tak Selamanya Error Itu Benar',q=q)
		# else:
		# 	redirect(url_for('solver'))


@app.route('/solver')
def solver():
	with open(os.path.join(APP_STATIC, 'solver.txt')) as f:
	    s = f.read().split('\n')
	# solver = open("../solver.txt","r")
	return render_template('solverlists.html',title='Chall-Solver',solver=s)


@app.route('/hint')
def hints():
	return render_template('gethint.html',title='How To Play?')


@app.route('/inputflag',methods=['GET','POST'])
def inputflag():
	if request.method == 'POST':
		if request.args.get("flag","") == session['flag']:
			return redirect(url_for("inputsolver"))
	else:
		return render_template('inputflag.html',title='Input Flag')

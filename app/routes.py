#!/usr/bin/python3

from app import app
from flask import render_template,redirect,url_for,request
from jinja2 import Environment
jinja = Environment()


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
				sapa = "Salam kenal ya "
				emot = "😊"
				return render_template('nama.html',title='Nama Hacker',sapa=sapa,nama=output,emot=emot)
			else:
				emot = "😓"
				sapa = ""
				return render_template('nama.html',title='Nama Hacker',sapa=sapa,nama=output,emot=emot)



@app.route('/solver')
def namaTeman():
	solver = [
	{
		'nama': {'teman':'Adam Maulana Yusuf'},
		'asal': {'tempat':'Bandung'}
	},
	{
		'nama': {'teman':'Ali Syam'},
		'asal': {'tempat':'Bekasi'}
	},
	{
		'nama': {'teman':'Jundi Al-Mubarok'},
		'asal': {'tempat':'Cirebon'}
	},
	{
		'nama': {'teman':'M. Shohib Al-Mahdhor'},
		'asal': {'tempat':'Bekasi'}
	},
	{
		'nama': {'teman':'M. Syahid Al-Ghuroba'},
		'asal': {'tempat':'Lampung'}
	}]
	return render_template('solverlists.html',title='Chall-Solver',solver=solver)


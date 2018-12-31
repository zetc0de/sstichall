#!/usr/bin/python3
from flask import Flask
from jinja2 import Environment

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q87654akhsg32&!>Sz\n\xec]/'

jinja = Environment()
from app import routes





#!/usr/bin/python3
from flask import Flask 
from jinja2 import Environment

app = Flask(__name__)
jinja = Environment()
from app import routes


import os
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from aluguel_de_roupas import app, db


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


import os
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from aluguel_de_roupas import app, db


@app.route('/')
def index():
    return render_template('index.html')



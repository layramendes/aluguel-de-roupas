import os
from flask import url_for

SECRET_KEY = 'projeto'

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'layramendes',
        senha = 'Robertinho123?',
        servidor = 'localhost',
        database = 'aluguel_de_roupas'
    )
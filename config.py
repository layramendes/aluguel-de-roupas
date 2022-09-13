import configparser

config_file = configparser.ConfigParser()
config_file.read("env.ini")

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB='mysql+mysqlconnector',
        usuario=config_file['mysql']['usuario'],
        senha=config_file['mysql']['senha'],
        servidor=config_file['mysql']['servidor'],
        database=config_file['mysql']['database']
    )
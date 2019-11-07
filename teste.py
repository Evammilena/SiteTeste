from flask import flask

app=Flask(__name__)

@app.rout('/')
def index():
    return "Pagina Inicial"


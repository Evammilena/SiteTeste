from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db = SQLAlchemy(app)

app.config[]'SQLALCHEMY_DATABASE_URL'] = 'sqlite://minhasmensagens.db'

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem =  db.Column(db.Text, nullable=False) #nao pode  ser falsa

    def __repre__(self):
        return '<<<MSG: %r>>>' %self.mensagem




@app.route('/')
def index():
    return render_template("index.html")

@app.route ('/nova-mensagem')
def novamensagem():
    return render_template("mensagens.html")

if __name__=="__main_" :
    app.run(debug=True)

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route ("/nova-mensagem")
def novamensagem():
    return render_template("mensagens.html")

if __name__ == "__main_" :

    app.run(debug=True)

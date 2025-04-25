from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    texto ='Hello Word!'
    return render_template('index.html', texto=texto)

@app.route('/sobre')
def sobre():
    return 'Aqui é a página sobre'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

DATA_FILE = 'data.csv'

def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def add_dados(Exercicio, Repeticoes, Series, Carga, Observacoes):
     with open(DATA_FILE, mode='a', newline='' , encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([Exercicio, Repeticoes, Series, Carga, Observacoes])

@app.route('/')
def home():
    dados = read_data()
    return render_template('home.html', dados=dados)

@app.route('/cadastar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        Exercicio = request.form['Exercicio']
        Repeticoes = request.form['Repeticoes']
        Series = request.form['Series']
        Carga = request.form['Carga']
        Observacoes = request.form['Observacoes']
        add_dados(Exercicio, Repeticoes, Series, Carga, Observacoes)
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/comparacao')
def comparacao():
    dados = read_data()
    return render_template('comparacao.html', dados=dados)

@app.route('/conta')
def conta():
    return render_template('conta.html')

if __name__ == '__main__':
    app.run(debug=True)
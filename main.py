from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imc')
def imc():
    return render_template('imc.html')

@app.route('/contatos')
def contato():
    return render_template('contatos.html')

@app.route('/planos')
def planos():
    return render_template('planos.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    altura = float(request.form['altura'])
    peso = float(request.form['peso'])

    imc = round(peso/(altura**2),2)
    
    if imc <= 18.4:
        classificacao = 'Abaixo do peso'
    elif imc > 18.5 and imc <= 24.9:
        classificacao = 'Peso Ideal'
    elif imc > 25 and imc <= 29.9:
        classificacao = 'Acima do peso'
    elif imc > 30 and imc <= 34.9:
        classificacao = 'Obesidade Grau I'
    elif imc > 35 and imc <= 50:
        classificacao = 'Obesidade Grau II'
    else:
        classificacao = 'Obesidade Grau III'

    return render_template('imc.html', imc=imc, classificacao=classificacao)

if __name__ == "__main__":
    app.run(debug=True)
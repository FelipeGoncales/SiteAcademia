from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def imc():
    return render_template('imc.html')

app.run(debug=True)
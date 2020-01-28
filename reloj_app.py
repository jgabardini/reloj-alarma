from flask import Flask, request, jsonify #, escape
from reloj import Reloj

app = Flask(__name__)

@app.route('/')
def root():
    ''' Place holder'''
    return 'API del reloj alarma'

@app.route('/api/alarma/sonar')
def alarma_sonar():
    reloj = Reloj()
    halarma = request.args.get("hora-alarma")
    reloj.definir_alarma(halarma)
    reloj.prender()
    hactual = request.args.get("hora-actual")
    sonar = reloj.sonar(hactual)

    return jsonify({'hora-alarma': halarma, 'hora-actual': hactual, "sonar": sonar})
    
from flask import Flask, render_template, request
from fabrica.estufa import FabricaEstufa
from fabrica.campo import FabricaCampo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    ambiente = request.form['ambiente']

    fabrica = FabricaEstufa() if ambiente == 'estufa' else FabricaCampo()

    sensor = fabrica.criar_sensor_temperatura()
    irrigacao = fabrica.criar_modulo_irrigacao()

    return render_template(
        'resultado.html',
        ambiente=ambiente.capitalize(),
        sensor=sensor.ler(),
        irrigacao=irrigacao.acionar()
    )

if __name__ == '__main__':
    app.run(debug=True)

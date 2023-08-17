from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    data = request.get_json()
    
    if "altura" not in data or "peso" not in data:
        return jsonify({"error": "Dados incompletos"}), 400
    
    altura = data["altura"]
    peso = data["peso"]
    
    if altura <= 0 or peso <= 0:
        return jsonify({"error": "Altura e peso devem ser valores positivos"}), 400
    
    imc = peso / (altura ** 2)
    
    resultado = {
        "altura": altura,
        "peso": peso,
        "imc": imc,
        "mensagem": "O cálculo do IMC foi realizado com sucesso."
    }
    
    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(debug=True)

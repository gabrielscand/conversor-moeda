from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    if not from_currency or not to_currency or not amount:
        return jsonify({"error": "Parâmetros faltando. Use ?from=USD&to=BRL&amount=10"}), 400

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({"error": "O valor deve ser numérico."}), 400

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Erro ao obter taxa de câmbio."}), 500

    data = response.json()

    if to_currency.upper() not in data["rates"]:
        return jsonify({"error": "Moeda de destino inválida."}), 400

    rate = data["rates"][to_currency.upper()]
    result = amount * rate

    return jsonify({
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount,
        "converted_amount": round(result, 2),
        "rate": rate
    })

if __name__ == "__main__":
    app.run(debug=True)

    from flask_cors import CORS




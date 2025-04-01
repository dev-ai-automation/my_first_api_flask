from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        # Lógica de suscripción
        token = request.args.get('token')
        if token == 'tu_token_verificacion':
            return "Suscripción confirmada", 200
        else:
            return "Token inválido", 403

    elif request.method == 'POST':
        # Lógica para recibir datos
        data = request.get_json()
        if data is None:
            return jsonify({"error": "No se recibieron datos"}), 400

        print("Datos recibidos:", data)
        return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
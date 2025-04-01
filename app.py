"""Ejemplo de Webhook con Flask"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta de suscripción (GET)
@app.route('/webhook', methods=['GET'])
def subscribe():
    """suscripción"""
    # Ejemplo de verificación con token
    token = request.args.get('token')
    if token == 'tu_token_verificacion':
        return "Suscripción confirmada", 200
    else:
        return "Token inválido", 403

# Ruta para recibir datos (POST)
@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    """Recibir datos en formato JSON"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No se recibieron datos"}), 400

    # Procesar la información recibida (aquí se imprime en la consola)
    print("Datos recibidos:", data)

    # Retornar estado 200 OK junto con un mensaje de confirmación
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
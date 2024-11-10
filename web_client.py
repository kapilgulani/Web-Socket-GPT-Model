from flask import Flask, jsonify, render_template
from flask_cors import CORS
from websockets.sync.client import connect

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Flask will now look inside the templates folder

@app.route('/start')
def start_communication():
    results = []
    with connect("ws://localhost:8765") as websocket:
        for i in range(1, 10001):
            websocket.send(f"Request [{i}] Hello world!")
            message = websocket.recv()
            results.append(f"Received: {message}")
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

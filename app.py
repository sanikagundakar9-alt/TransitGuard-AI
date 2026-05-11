from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_eta', methods=['POST'])
def predict_eta():
    data = request.json
    distance = data.get('distance', 0)
    avg_speed = 20 
    eta = (distance / avg_speed) * 60
    return jsonify({"eta": round(eta, 2)})

if __name__ == '__main__':
    app.run(debug=True)
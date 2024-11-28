from flask import Flask, request, jsonify
import pickle
import pandas as pd
from preprocessing import preprocess_data
from model import train_model, retrain_model, predict, check_data_drift

app = Flask(__name__)

# Load the trained model
MODEL_PATH = './model/student-predictor.pkl'
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    df = pd.DataFrame(data)
    preprocessed_data = preprocess_data(df)
    predictions = predict(model, preprocessed_data)
    return jsonify(predictions)

@app.route('/retrain', methods=['POST'])
def retrain_route():
    new_data = request.get_json()
    new_df = pd.DataFrame(new_data)
    global model
    model = retrain_model(new_df)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    return jsonify({"message": "Model retrained successfully!"})

@app.route('/check_drift', methods=['POST'])
def check_drift_route():
    old_data = request.files['old_data'].read()
    new_data = request.files['new_data'].read()
    old_df = pd.read_csv(old_data)
    new_df = pd.read_csv(new_data)
    drift_detected = check_data_drift(old_df, new_df)
    return jsonify({"drift_detected": drift_detected})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

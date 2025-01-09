from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the saved Random Forest model
model = joblib.load("predictive_maintenance_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict RUL.
    Input: JSON data with sensor readings.
    Output: Predicted RUL.
    """
    data = request.get_json()  # Get input data as JSON
    input_df = pd.DataFrame(data)  # Convert JSON to DataFrame
    prediction = model.predict(input_df)  # Make predictions
    return jsonify({"RUL_prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)

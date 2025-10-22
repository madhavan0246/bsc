from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# Define prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json(force=True)

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Predict
        prediction = model.predict(df)[0]

        return jsonify({
            "status": "success",
            "input": data,
            "prediction": prediction
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

# Run server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

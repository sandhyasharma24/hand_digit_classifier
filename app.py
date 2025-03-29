from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import os

# Load the trained model
model = tf.keras.models.load_model("mnist_model.h5")

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello World!"})

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    img = Image.open(io.BytesIO(file.read())).convert("L")  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to match the model input
    img = np.array(img) / 255.0  # Normalize
    img = img.reshape(1, 28, 28, 1)  # Reshape for the model

    prediction = model.predict(img)
    predicted_digit = np.argmax(prediction)

    return jsonify({"prediction": int(predicted_digit)})

@app.route("/")
def home():
    return "Hello, Flask is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get PORT from environment variable
    app.run(host="0.0.0.0", port=port, debug=True)  # Ensure it binds to 0.0.0.0

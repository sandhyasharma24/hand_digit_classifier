# Handwritten Digit Classifier API

This is a Flask-based API for classifying handwritten digits using a trained deep learning model (MNIST). It allows users to send an image of a digit and get a prediction in return.

## Features
- **Predict Handwritten Digits**: Upload an image of a digit (0-9), and the API returns its predicted class.
- **RESTful API**: Simple GET and POST endpoints for interaction.
- **Model Loading**: Uses a pre-trained TensorFlow/Keras model (`mnist_model.h5`).
- **Docker-Ready**: Easily deployable using Docker.
- **Render Deployment**: Can be deployed on Render or similar platforms.

---

## Installation & Setup

### **1. Clone the Repository**
```sh
git clone <your-repo-url>
cd <your-project-folder>
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run the API Locally**
```sh
python app.py
```
The API will start on `http://127.0.0.1:5000/`.

---

## API Endpoints

### **1. Health Check**
- **Endpoint**: `/test`
- **Method**: `GET`
- **Response**:
```json
{
  "message": "Hello World!"
}
```

### **2. Predict Digit**
- **Endpoint**: `/predict`
- **Method**: `POST`
- **Request**: Multipart form-data with an image file (`file` key)
- **Response**:
```json
{
  "prediction": 5
}
```

---

## Deployment on Render

### **1. Push to GitHub**
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### **2. Deploy on Render**
1. Go to [Render](https://render.com/).
2. Click on **New Web Service**.
3. Connect your GitHub repository.
4. Set **Build Command**: `pip install -r requirements.txt`
5. Set **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
6. Deploy & Check Logs!

---

## Future Enhancements
- ✅ Add support for multiple model architectures.
- ✅ Improve preprocessing for better accuracy.
- ✅ Deploy as a Docker container.

---

## License
This project is licensed under the MIT License.


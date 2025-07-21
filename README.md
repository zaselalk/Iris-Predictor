# Iris-Predictor
A simple end-to-end machine learning project that predicts iris flower species using a trained ML model exposed through a REST API.



**Iris Predictor** is a simple end-to-end machine learning project that:
- Trains a Random Forest model to classify iris flowers.
- Serves predictions through a Flask REST API.
- Includes scripts for training, testing, and deploying the model.

---

## 🚀 Features
- **End-to-End Workflow:** Data loading, model training, API serving.
- **REST API Endpoint:** Predicts iris species based on flower measurements.
- **Simple web page to interact** - using html, css and js
- **Lightweight Stack:** Uses Python, scikit-learn, and Flask.
- **Ready for Deployment:** Easily containerized and deployable to cloud services.

---

## 🗂 Project Structure
iris-predictor/
├── data/
│ └── iris.csv
├── train_model.py
├── app.py
├── test_predict.py
└── README.md

## 🔧 Installation & Setup

### 1. Clone the Repo
```bash
git clone https://github.com/<your-username>/iris-predictor-api.git
cd iris-predictor-api
```

### 2. Install dependencies
```bash
pip install numpy pandas scikit-learn flask joblib requests
```

### 3. Train the Model
```python
python train_model.py

```

### 3. Start the API
```
python app.py

```

## 4. Visit the prediction page
`http://127.0.0.1:5000/predict`



## 📜 License
MIT License. Feel free to use and modify.


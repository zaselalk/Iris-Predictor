# Iris-Predictor
A simple end-to-end machine learning project that predicts iris flower species using a trained ML model exposed through a REST API and simple web application.

I have create this github repo to get idea about how to train and use simple AI model. feel free to experiment with yourself with the repo

The iris flower, scientifically known as Iris, is a distinctive genus of flowering plants. Within this genus, there are three primary species: Iris setosa, Iris versicolor, and Iris virginica

![MasterHead](https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification-1024x367.png)

<font size="1">Image Courtesy: https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification-1024x367.png</font>

The objective of the project is to to develop a machine learning model and create simple html interface capable of learning from the measurements of iris flowers and accurately classifying them into their respective species.


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


## Similar Projects
https://github.com/Apaulgithub/oibsip_taskno1

While searching for similar projects, I came across the above GitHub repository. It provided valuable insights, especially regarding the visualization and structure of the Iris flower dataset. I recommend checking out that project for additional ideas and inspiration.


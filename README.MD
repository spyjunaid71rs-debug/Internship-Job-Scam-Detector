# 🛡 Internship Scam Detector using Machine Learning

An AI-powered Internship Scam Detection System that predicts whether an internship posting is **Genuine** or **Fake** using Machine Learning.

The project uses a **Random Forest Classifier** with **Hyperparameter Tuning**, a **FastAPI backend**, and a modern web interface to analyze internship details and provide a fraud prediction along with confidence score, risk level, and reasons.

---

# 🚀 Demo

### Genuine Internship

- ✅ Prediction: Genuine Internship
- 📊 Confidence Score
- 🟢 Low Risk
- 📋 Reasons for Prediction

### Fake Internship

- ❌ Prediction: Fake Internship
- 📊 Confidence Score
- 🔴 High Risk
- 📋 Reasons for Prediction

---

# ✨ Features

- 🤖 Machine Learning based Internship Scam Detection
- 🌲 Random Forest Classifier
- ⚙ Hyperparameter Tuning using RandomizedSearchCV
- 🚀 FastAPI REST API
- 🎨 Interactive Frontend (HTML, CSS & JavaScript)
- 📈 Confidence Score
- ⚠ Risk Level Detection
- 📄 Reason-Based Prediction
- 🌐 Company Website Verification
- 💼 LinkedIn Profile Verification
- 📧 Recruiter Email Domain Analysis
- 💰 Registration Fee Detection
- 💳 Payment Requirement Detection

---

# 🧠 Machine Learning Pipeline

Dataset

⬇

Data Cleaning

⬇

Missing Value Handling

⬇

Feature Engineering

⬇

One-Hot Encoding

⬇

Train-Test Split

⬇

Random Forest Classifier

⬇

Hyperparameter Tuning

⬇

Model Evaluation

⬇

FastAPI Deployment

⬇

Frontend Integration

---

# 📊 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **83.55%** |
| Precision | **69.57%** |
| Recall | **46.02%** |
| F1 Score | **55.39%** |
| ROC-AUC | **84.14%** |

---

# 🎯 Classification

Binary Classification

- **0 → Genuine Internship**
- **1 → Fake Internship**

---

# 📂 Input Features

The trained model uses **40 engineered features**, including:

- Internship Title
- Employment Type
- Work Mode
- Industry
- Location
- Company Size
- Website Availability
- LinkedIn Presence
- Recruiter Email Type
- Stipend
- Registration Fee
- Payment Required
- Fake Certificate Offer
- Suspicious Email Domain

---

# 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML5
- CSS3
- JavaScript

### Model Saving

- Joblib

---

# 📁 Project Structure

```
Internship-Scam-Detector/

│── app.py
│── internship_scam_detector.pkl
│── requirements.txt
│── README.md

├── schemas/
│      input_schema.py

├── utils/
│      model_loader.py
│      input_processor.py
│      predictor.py

├── templates/
│      index.html

├── static/
│      style.css
│      script.js

└── Internship Scam Detector.ipynb
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Internship-Scam-Detector.git
```

Move into the project

```bash
cd Internship-Scam-Detector
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI server

```bash
uvicorn app:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

---

# 📸 Screenshots

### Home Page

(Add Screenshot Here)

---

### Genuine Internship Prediction

(Add Screenshot Here)

---

### Fake Internship Prediction

(Add Screenshot Here)

---

# 🔮 Future Improvements

- Deep Learning Models
- XGBoost & LightGBM Comparison
- Explainable AI (SHAP)
- Email Verification API
- Company Reputation Checker
- Resume Matching
- Cloud Deployment

---

# 👨‍💻 Author

**Junaid Hussain**

B.Tech – Computer Science & Engineering (AI & ML)

Machine Learning | Deep Learning | Generative AI | FastAPI | Python

---

# ⭐ If you like this project

Please consider giving this repository a **Star ⭐**.

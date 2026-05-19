# 📧 Email Spam Detector

A Machine Learning-based web application that classifies email messages as **Spam** or **Ham (Not Spam)** using **TF-IDF Vectorization** and the **Multinomial Naive Bayes** algorithm. The application is built with Flask and provides a simple and intuitive web interface for real-time spam detection.

---

## 🚀 Features

- 📧 Detects whether an email is Spam or Not Spam
- 🧠 Machine Learning model using Multinomial Naive Bayes
- 🔤 Text feature extraction with TF-IDF Vectorizer
- 🌐 Interactive web interface built with Flask
- 💾 Trained model and vectorizer saved with Pickle
- ☁️ Ready for deployment on Render, Railway, AWS EC2, and PythonAnywhere

---

## 🛠️ Tech Stack

| Category | Technologies |
|--------|--------|
| Programming Language | Python 3 |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| Model Serialization | Pickle |

---

## 📂 Project Structure

```text
Email_Spam_Detector/
│
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css

📧 Email Spam Detector

A machine learning-based web application that classifies emails as Spam or Not Spam (Ham) using Scikit-learn and Flask. The model is trained using TF-IDF Vectorization and the Multinomial Naive Bayes algorithm, which is highly effective for text classification tasks.

🚀 Live Demo

Add your deployed application URL here:

https://your-email-spam-detector.onrender.com
📌 Features
📧 Detects whether an email is Spam or Ham
🧠 Machine Learning model using Multinomial Naive Bayes
🔤 Text preprocessing with TF-IDF Vectorizer
🌐 User-friendly Flask web interface
💾 Model and vectorizer saved using pickle
☁️ Ready for deployment on Render, Railway, or AWS EC2
🛠️ Technologies Used
Python Software Foundation (Python 3.x)
Flask
Scikit-learn
Pandas
NumPy
HTML5
CSS3
Pickle
📂 Project Structure
Email_Spam_Detector/
│── app.py
│── train_model.py
│── spam.csv
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
🧠 Machine Learning Workflow
Load and clean the dataset
Convert text into numerical features using TF-IDF
Split data into training and testing sets
Train the Multinomial Naive Bayes model
Evaluate model accuracy
Save the trained model and vectorizer
Build a Flask web interface
Predict user-entered email text
📊 Model Performance
Metric	Score
Accuracy	97% – 99%
Algorithm	Multinomial Naive Bayes
Feature Extraction	TF-IDF Vectorizer

Performance may vary depending on the dataset used.

📥 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/Email_Spam_Detector.git
cd Email_Spam_Detector
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Train the Model
python train_model.py
6️⃣ Run the Flask App
python app.py
7️⃣ Open in Browser
http://127.0.0.1:5000
📝 Example Input
Congratulations! You have won a free iPhone. Click here to claim now!
Output
Spam
📦 requirements.txt
Flask
scikit-learn
pandas
numpy
🌍 Deployment Options
Render
Railway
AWS EC2
PythonAnywhere
🎯 Future Improvements
Deep learning using TensorFlow or PyTorch
Ensemble learning models
Email attachment scanning
Real-time API integration
Docker containerization with Docker
👨‍💻 Author

Elbert
Python Developer | Machine Learning Enthusiast

GitHub: https://github.com/your-username
LinkedIn: https://linkedin.com/in/your-profile
⭐ Support

If you found this project useful, please give it a ⭐ on GitHub and share it with others.

📜 License

This project is licensed under the MIT License.

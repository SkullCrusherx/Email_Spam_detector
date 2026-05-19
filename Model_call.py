from flask import Flask,render_template,request
import joblib
saved = joblib.load('spam_detection_model.pkl')


app = Flask(__name__)
@app.route('/email')
def home():
    return render_template('Email_detector.html')


@app.route('/predict', methods=['POST'])
def submit():
    model = saved['model']
    tfidf = saved['tfidf']
    email = request.form.get('email_text')
    email_tfidf = tfidf.transform([email])
    prediction = model.predict(email_tfidf)
    return render_template('spam_result.html', prediction=prediction[0])


if __name__ == "__main__":
    app.run(debug=True)
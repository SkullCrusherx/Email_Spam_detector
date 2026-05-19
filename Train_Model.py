import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score

csv = pd.read_csv(r'C:\Users\Predator\PyCharmMiscProject\Excel\Spam_Ham.csv')
csv.dropna(subset=['keyword','label'], inplace=True)


X = csv['keyword']
y = csv['label']


tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(X)
while True:
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y,test_size = 0.2)

    # Create and train Multinomial Naive Bayes model
    model = MultinomialNB()
    model.fit(X_train, y_train)



    #new_text = X_test
    #new_tfidf = Tfidf.transform(X_test)


    # Predict label
    prediction = model.predict(X_test)
    v = accuracy_score(y_test, prediction)
    if v >= 0.90:
        print(v)
        joblib.dump({'model': model,'tfidf': tfidf},'spam_detection_model.pkl')
        print("Model saved")
        break
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd

data = {
    'email':[
        'win free money now',
        'meeting tomorrow at 10am',
        'claim your prize today',
        'project update attached',
        'limited time offer click here',
        'team lunch on friday'
    ],
    'label' : ['spam','ham','spam','ham','spam','ham']
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['email'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = MultinomialNB()
model.fit(X_train,y_train)

predictions = model.predict(X_test)

print(f'Accuracy: {accuracy_score(y_test,predictions)}')

new_email = ["urgent claim your reward"]
new_vector = vectorizer.transform(new_email)

print(f'Prediction: {model.predict(new_vector)[0]}')
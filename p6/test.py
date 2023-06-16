import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



data = pd.read_csv('p-tennis.csv')

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

# print(x.head())
# print(y.head())

le_outlook = LabelEncoder()
x.Outlook = le_outlook.fit_transform(x.Outlook)

le_temprature = LabelEncoder()
x.Temperature = le_temprature.fit_transform(x.Temperature)

le_humidity = LabelEncoder()
x.Humidity = le_humidity.fit_transform(x.Humidity)

le_windy = LabelEncoder()
x.Windy = le_windy.fit_transform(x.Windy)

le_pt = LabelEncoder()
print(y)
y = le_pt.fit_transform(y)


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

nb_classifier = GaussianNB()
nb_classifier.fit(x_train,y_train)

print(nb_classifier.predict(x_test))
print(y_test)

print("Accuracy is:", accuracy_score(nb_classifier.predict(x_test), y_test))
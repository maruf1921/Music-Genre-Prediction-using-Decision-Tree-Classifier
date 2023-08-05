import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('music.csv')
X = df.drop(columns=['genre'])
Y = df['genre']

model = DecisionTreeClassifier()
model.fit(X, Y)
predictions = model.predict([[22,1], [22,0]])
print(predictions)
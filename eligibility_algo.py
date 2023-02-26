import pandas as pd
from sklearn.tree import DecisionTreeClassifier

area_code = int(input("Enter the area code(Urban = 1 and Rural = 0)"))
    
elec = float(input("Enter the amount of surplus solar energy produced: "))

appli = pd.read_csv("database.csv")
X = appli.drop(columns = ["Earnings"])
y = appli["Earnings"]

model = DecisionTreeClassifier()
model.fit(X, y)

predct = model.predict([[area_code, elec]])

print(predct)
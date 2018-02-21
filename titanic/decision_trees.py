import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Read data from CSV
df = pd.read_csv("titanic.csv", index_col="PassengerId")

# Deleting rows with NaN values
data = df.replace(["female", "male"], [0, 1])
filtered_data = data[["Sex", "Age", "Pclass", "Fare", "Survived"]].dropna()

# Columns for DecisionTree
columns = ["Sex", "Age", "Pclass", "Fare"]

X = filtered_data[columns].values.tolist()
y = filtered_data["Survived"].values.tolist()

clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, y)

importances = clf.feature_importances_

importances_dict = dict(zip(columns, importances))
sorted_values = sorted(importances_dict, key=importances_dict.get, reverse=True)

with open("importance.txt", mode="w") as f:
    f.write(f"{sorted_values[0]} {sorted_values[1]}")


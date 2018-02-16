import pandas as pd

data = pd.read_csv("titanic.csv", index_col="PassengerId")
count_sex = data["Sex"].value_counts()

with open("count_sex.txt", mode="w") as f:
    f.write(f"{count_sex['male']} {count_sex['female']}")

count_survived = data["Survived"].value_counts()
per_survived = round(count_survived[1]/(count_survived[0]+count_survived[1]) * 100, 2)

with open("count_survived.txt", mode="w") as f:
    f.write(f"{per_survived}")

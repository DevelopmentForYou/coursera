import pandas as pd

data = pd.read_csv("titanic.csv", index_col="PassengerId")
count_sex = data["Sex"].value_counts()

with open("count_sex.txt", mode="w") as f:
    f.write(f"{count_sex['male']} {count_sex['female']}")

count_survived = data["Survived"].value_counts()
per_survived = round(count_survived[1]/sum(count_survived) * 100, 2)

with open("count_survived.txt", mode="w") as f:
    f.write(f"{per_survived}")

count_first_class = data["Pclass"].value_counts()
per_first_class = round(count_first_class[1]/sum(count_first_class) * 100, 2)

with open("count_first_class.txt", mode="w") as f:
    f.write(f"{per_first_class}")

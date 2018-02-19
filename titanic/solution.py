import os

import pandas as pd

if not os.path.exists("output"):
    os.mkdir(path="output")


def write_file(filename, data_to_file):
    with open(os.path.join("output", filename), mode="w") as f:
        f.write(data_to_file)


data = pd.read_csv("titanic.csv", index_col="PassengerId")
count_sex = data["Sex"].value_counts()

write_file(filename="count_sex.txt", data_to_file=f"{count_sex['male']} {count_sex['female']}")

count_survived = data["Survived"].value_counts()
per_survived = round(count_survived[1] / sum(count_survived) * 100, 2)

write_file(filename="count_survived.txt", data_to_file=f"{per_survived}")

count_first_class = data["Pclass"].value_counts()
per_first_class = round(count_first_class[1] / sum(count_first_class) * 100, 2)

write_file(filename="count_first_class.txt", data_to_file=f"{per_first_class}")

age_mean = data["Age"].mean()
age_median = data["Age"].median()

write_file(filename="age_mean.txt", data_to_file=f"{round(age_mean, 2)} {age_median}")

corr = data["SibSp"].corr(data["Parch"], method="pearson")

write_file(filename="corr.txt", data_to_file=f"{round(corr, 2)}")

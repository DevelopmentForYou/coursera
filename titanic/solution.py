import pandas

data = pandas.read_csv("titanic.csv", index_col="PassengerId")
count_sex = data["Sex"].value_counts()


with open("count_sex.txt", mode="w") as f:
    f.write(f"{count_sex['male']} {count_sex['female']}")

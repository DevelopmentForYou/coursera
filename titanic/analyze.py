import re
from collections import Counter

import pandas as pd

from titanic.file import write_file

# Read data from CSV
data = pd.read_csv("titanic.csv", index_col="PassengerId")
# Counting gender
count_sex = data["Sex"].value_counts()

write_file(sub_dirname="analyze", filename="count_sex.txt", data_to_file=f"{count_sex['male']} {count_sex['female']}")

# Counting survived
count_survived = data["Survived"].value_counts()
per_survived = round(count_survived[1] / sum(count_survived) * 100, 2)

write_file(sub_dirname="analyze", filename="count_survived.txt", data_to_file=f"{per_survived}")

# Counting people of first class
count_first_class = data["Pclass"].value_counts()
per_first_class = round(count_first_class[1] / sum(count_first_class) * 100, 2)

write_file(sub_dirname="analyze", filename="count_first_class.txt", data_to_file=f"{per_first_class}")

# Counting mean and median of age
age_mean = data["Age"].mean()
age_median = data["Age"].median()

write_file(sub_dirname="analyze", filename="age_mean.txt", data_to_file=f"{round(age_mean, 2)} {age_median}")

# Counting correlation between SibSp and Parch
corr = data["SibSp"].corr(data["Parch"], method="pearson")

write_file(sub_dirname="analyze", filename="corr.txt", data_to_file=f"{round(corr, 2)}")

# Finding the most popular female name on the ship
female_fullnames = data.loc[(data["Sex"] == "female"), ["Name"]]["Name"]
female_names = []

for name in female_fullnames:
    if "Mrs." in name:
        try:
            female_names.append(re.findall(r"\((.*)\)", name)[0].split()[0])
        except IndexError:
            pass
    elif "Miss." in name:
        try:
            female_names.append(re.findall("(Miss.)\s(.+)", name)[0][1].split()[0])
        except IndexError:
            pass

count_names = Counter(female_names)
most_popular_name = max(count_names, key=count_names.get)

write_file(sub_dirname="analyze", filename="most_popular_name.txt", data_to_file=f"{most_popular_name}")

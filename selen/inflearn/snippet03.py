import csv

f = open("output01.csv", "r", encoding="utf-16")
fr = csv.reader(f)
for row in fr:
    print(row)

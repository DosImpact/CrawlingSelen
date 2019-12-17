import csv

f = open("output.csv", "r", encoding="utf-16")
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()

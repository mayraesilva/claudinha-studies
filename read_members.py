import csv

with open("members.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['first_name']} {row['last_name']}")

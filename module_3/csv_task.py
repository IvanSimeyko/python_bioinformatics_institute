import operator
import csv


def first_task():
    d = {}
    with open('Crimes.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2][6:10] == '2015':
                if row[5] not in d:
                    d[row[5]] = 1
                else:
                    d[row[5]] += 1

    print(max(d, key=lambda i: d[i]))

first_task()

import operator
import csv
import json

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

#first_task()

# code second task

import sys
sys.stdin = open("class.json", "r")
d = {}
ans = {}


def check(child, parents):
    """
    Доделать фуннкцию!!!
    """

def second():
    f = input()
    data = json.loads(f)
    print(data)
    for i in data:
        print(i)
        d[i['name']] = i['parents']
    print(d)

# for key, value in sorted(ans.items()):  # Note the () after items!
#     print(key, ':', value)


second()

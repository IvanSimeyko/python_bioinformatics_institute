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


def check(d, child, parents):
    """
    Функция проверки предков и наследников
    """
    if child not in ans:
        ans[child] = 1
    if len(parents) > 0:
        for i in parents:
            if i not in ans:
                ans[i] = 1
            ans[i] += 1
        for j in d:
            if child in d[j] and i not in d[j]:
                ans[i] += 1
    return ans

def input_date():
    f = input()
    data = json.loads(f)
    #print(data)
    # make dictionary
    for i in data:
        #print(i)
        d[i['name']] = i['parents']
    print(d)
    for elem in d:
        check(d, elem, d[elem])
    for key, value in sorted(ans.items()):  # Note the () after items!
        print(key, ':', value)

input_date()
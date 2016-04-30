import datetime
import simplecrypt

# date = input('Enter date: ').split()
# num_days = int(input('Enter number of days: '))

def res(date, num_days):
    res = ''
    x = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    ans = x + datetime.timedelta(num_days)
    for i in (ans.year, ans.month,  ans.day):
        res += str(i) + ' '
    return res

# print(res(date, num_days))

def a(a, l):
    if a == 5:
        return 'yes'
    else:
        for i in l:
            return a(i, l)

print(a(3, [1,2,3,4,5,6]))



import datetime

date = input('Enter date: ').split()
num_days = int(input('Enter number of days: '))

def res(date, num_days):
    res = ''
    x = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    ans = x + datetime.timedelta(num_days)
    for i in (ans.year, ans.month,  ans.day):
        res += str(i) + ' '
    return res

print(res(date, num_days))

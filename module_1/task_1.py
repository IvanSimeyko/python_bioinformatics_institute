__author__ = 'Ivan'

'''
Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.
'''
i, ans = 0, 0
n = int(input())
while i < n:
    ans += int(input())
    i += 1
print (ans)
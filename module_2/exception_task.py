# def foo():
#     pass
# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError ")
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print("AssertionError")
#
# class NonPositiveError(Exception):
#     pass
#
# class PositiveList(list):
#
#     def append(self, p_object):
#         if p_object > 0:
#              x = super(PositiveList, self).append(p_object)
#              return x
#         elif p_object <= 0:
#             raise NonPositiveError(str(p_object) + ' is not positive number')

# a = PositiveList([1,2,3])
# a.append(4)
# print(a)
# a.append(-4)

# try:
#     x = 5 / 0
# except ArithmeticError:
#     print('hello world')
#
# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print('division by zero')
#

import sys
sys.stdin = open("input.txt", "r")

ans = []
par = []


def check(exs):
    for i in d[exs]:
        if i in par:
            return True
    for i in d[exs]:
        if check(i):
            return True

d, k = {}, 0
n = int(input('Enter number of string: '))
while k < n:
    in_put = input('Enter class name: ').split(' : ')
    if len(in_put) == 1:
        d[in_put[0]] = []
    else:
        d[in_put[0]] = in_put[1].split()
    if len(in_put) > 1:
        for i in in_put[1].split():
            if i not in d:
                d[i] = []
    k += 1

print(d)

n = int(input("Enter number questions: "))
k = 0
while k < n:
    exs = input('Enter question: ')
    if check(exs):
        ans.append(exs)
    par.append(exs)
    #print(par)
    k += 1

print(ans)
for i in ans:
    print(i)

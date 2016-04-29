class DoubleElementListIterator:
    """
    Пример класса, который при итерации возрацает
    по два элемента
    """

    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

# x = DoubleElementListIterator([1, 2])
# print(next(x))
# print(next(x))
# print(next(x))


class multifilter:

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge

    def __iter__(self):
        return self


    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg.)
        pass

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        pass

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        pass

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

#print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

import itertools
ans = []
def is_simple(n):
    d = n - 1
    while d > 1:
        if n % d == 0:
            return False
        d -= 1
    return True

def primes():
    x = 2
    while True:
        if is_simple(x):
            yield x
            x += 1
        else:
            x += 1
            continue

#print(list(itertools.takewhile(lambda x: x <= 31, primes())))

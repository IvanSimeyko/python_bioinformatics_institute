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


class multifilter:

    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg.)
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge
        self.i = 0

    def __iter__(self):
        """
        Возвращаем самого себя
        """
        return self

    def __next__(self):
        """
        Перебираем при итерации по одному элементу
        """
        if self.i < len(self.iterable):
            self.i += 1
            pos = 0
            neg = 0
            #return self.iterable[self.i - 1]
            for func in self.funcs:
                if func(self.iterable[self.i-1]):
                    pos += 1
                    #return self.iterable[self.i-1]
                else:
                    neg += 1
                    #return next(self)
            if self.judge(pos, neg):
                return self.iterable[self.i-1]
            else:
                return next(self)
        else:
            raise StopIteration



def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# x = multifilter(a, mul2, mul3, mul5)
# print(next(x))

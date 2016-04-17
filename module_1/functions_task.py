a = []
def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))
#print(a)


def closest_mod_5(x):
    """
    x - целое число
    возвращаем число которое:
        больше или равно x
        делится нацело на 5
    """
    if x % 5 == 0:
         return x
    for i in range(1,5):
        if (i+x) % 5 == 0:
            return i+x

#x = closest_mod_5(13); print(x)

# рекурсивная функция на примере чисел Фибоначчи
def fib(x):
    """
    не очень зорошая идея вычислять так числа Фибоначчи. Подробнее -
    добро пожаловать в курс по алгоритмам
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
#print(fib(7))

# решение последней задачи в 1.3
n, k = map(int, input().split())
def num_soch(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        f = num_soch(n-1, k) + num_soch(n-1, k-1)
        return f
print(num_soch(n, k))

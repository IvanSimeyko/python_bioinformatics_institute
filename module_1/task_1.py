def sum_of_number():
    """
    Вашей программе на вход подается последовательность строк.
    Первая строка содержит число n (1 ≤ n ≤ 100).
    В следующих n строках содержится по одному целому числу.
    Вычислиь сумму этих чисел
    """

    i, ans = 0, 0
    n = int(input())
    while i < n:
        ans += int(input())
        i += 1
    print (ans)


def various_object(*objects):
    """
    Функция,которая вычисляет количество различных объектов в списке.
    Два объекта a и b считаются различными, если a is b равно False.
    """
    ans = 0
    res = set()
    for obj in objects:
        if id(obj) not in res:
            res.add(id(obj))
            ans += 1
    print(res, ans)

various_object(1, 2, 1, 2, 3, True)


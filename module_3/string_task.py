def check_contain():
    """
    Решение задачи 3.2 шаг 6
    """
    # get value of variable from user
    s, a, b = [input('Enter value in var: ').strip() for _ in range(3)]
    num = []

    if a in b and a in s:
        print('Impossible')
    else:
        while a in s:
            num.append('1')
            s = s.replace(a, b)
        print(len(num))


def a(c, d):
    def b(c=c, d=d):
        if d > 0:
            d -= 1
            return  d +c
    return b

# x = a(5, 1)
# print(x())

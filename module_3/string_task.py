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

def check_contain_2():
    """
    Решение задачи 3.2 шаг 7
    """
    s, t = [input('Enter value: '). strip() for _ in range(2)]
    x = sum(s[i:].startswith(t) for i in range(len(s)))
    print(x)
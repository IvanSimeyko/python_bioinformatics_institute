class MoneyBox:
    value = 0

    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.value + v <= self.capacity:
            return True
        return False

    def add(self, v):
        # положить v монет в копилку
        self.value += v
        return self.value

# x = MoneyBox(10)
# x.add(7)
# print(x.value)
# print(x.add(1))
# print(x.value)

class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.val = []

    def summa(self, val):
        while len(val) >= 5:
            x = sum(val[:5])
            print(x)
            del(val[:5])

    def add(self, *a):
        # добавить следующую часть последовательности
        self.val.extend(a)
        if len(self.val) >= 5:
            self. summa(self.val)

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return self.val

# buf = Buffer()
# buf.add(1, 2, 3)
# print(buf.get_current_part()) # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# print(buf.get_current_part()) # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# print(buf.get_current_part()) # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# print(buf.get_current_part()) # вернуть [1]

class ExtendedStack(list):
    def sum(self):
        # операция сложения
        x = self.pop()
        y = self.pop()
        self.append(x+y)

    def sub(self):
        # операция вычитания
        x = self.pop()
        y = self.pop()
        self.append(x-y)

    def mul(self):
        # операция умножения
        x = self.pop()
        y = self.pop()
        self.append(x*y)

    def div(self):
        # операция целочисленного деления
        x = self.pop()
        y = self.pop()
        self.append(x//y)

# x = ExtendedStack([5, 11])
# x.div()
# print(x)

import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):

    def append(self, elem):
        x = super(LoggableList, self).append(elem)
        self.log(elem)
        return x

x = LoggableList()
print(x)
x.append(4)
print(x)
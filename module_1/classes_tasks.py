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

x = MoneyBox(10)
x.add(7)
print(x.value)
print(x.add(1))
print(x.value)

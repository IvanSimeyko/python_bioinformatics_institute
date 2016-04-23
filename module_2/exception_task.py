def foo():
    pass
try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError ")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")

class NonPositiveError(Exception):
    pass

class PositiveList(list):

    def append(self, p_object):
        if p_object > 0:
             x = super(PositiveList, self).append(p_object)
             return x
        elif p_object <= 0:
            raise NonPositiveError(str(p_object) + ' is not positive number')

# a = PositiveList([1,2,3])
# a.append(4)
# print(a)
# a.append(-4)

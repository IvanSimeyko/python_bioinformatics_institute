# https://stepic.org/lesson/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0-%D0%B8%D0%BC%D1%91%D0%BD-%D0%B8-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8-%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8-24460/step/8?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6766
ans = {
    'global':{'parents': None,'vars': []}
    }
car_ns = ['global']

def add(name_space, name_var):
    """
    function for created variable
    """
    ans[name_space]['vars'].append(name_var)
    return ans

def create(name_fun, name_space):
    """
    create name space
    """
    ans[name_space]['vars'].append(name_fun)
    ans[name_fun] = {'parents': name_space, 'vars': []}
    car_ns.append(name_fun)
    return ans, car_ns

def get(name_space, var):
    if var in ans[name_space]['vars']:
        print(name_space)
    elif ans[name_space]['parents'] is None:
        print(None)
    else:
        return get(ans[name_space]['parents'], var)
    pass

n = int(input("Enter number string"))
k = 0
while k < n:
    cmd, namesp, arg = input().split()
    if cmd == "add":
        add(namesp, arg)
    elif cmd == 'create':
        create(namesp, arg)
    elif cmd == 'get':
        get(namesp, arg)
    k +=1

# add('global', 'a')
# create('foo', 'global')
# add('foo', 'b')
# get('foo', 'c')
# create('bar', 'foo')
# add('bar', 'a')
# print(ans)
# print(car_ns)
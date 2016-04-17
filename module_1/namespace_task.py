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
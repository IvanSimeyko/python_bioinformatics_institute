import re

# video examples
pattern = r'abc'
string = r'dabc'
match_object = re.search(pattern, string)
print('match_object=', match_object)

pattern = r'a[a-zA-Z]c'  # любая буква
string = r'abc'
match_object = re.match(pattern, string)
print('match_object= ', match_object)

string = 'abc, acc, bbc'
all_inclusions = re.findall(pattern, string)
print('all_inclusions= ', all_inclusions)

fixed_typos = re.sub(pattern, 'abc', string)
print('fixed_typos= ', fixed_typos)

#example with interrogatory(?)
pattern = r'english\?'
string = r'Do you speak english?'
match_object = re.search(pattern, string)
print('match_object= ', match_object)

#example with ( )
pattern = r'(test|text)*'
string = r'testtext'
test = re.match(pattern, string)
print('test= ', test)

#example with groups
pattern = r'Hello (abc|test)'
string = r'Hello abc'
test = re.match(pattern, string)
print('test= ', test)
print(test.group())    # 0 задан аргументом по умолчанию

#example with groups
pattern = r'(\w*)-\1'    # \1 - номер группы
string = r'test-test'
test = re.match(pattern, string)
print('test= ', test)
print(test.group())    # 0 задан аргументом по умолчанию
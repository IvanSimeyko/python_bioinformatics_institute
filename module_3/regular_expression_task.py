import re

# video examples
pattern = r'abc'
string = r'dabc'
match_object = re.search(pattern, string)
#print(match_object)

pattern = r'a[a-zA-Z]c'  # любая буква
string = r'abc'
match_object = re.match(pattern, string)
print(match_object)

string = 'abc, acc, bbc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)

#example with interrogatory(?)
pattern = r'english\?'
string = r'Do you speak english?'
match_object = re.search(pattern, string)
print(match_object)

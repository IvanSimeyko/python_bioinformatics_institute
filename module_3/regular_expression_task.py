import re
#
# # video examples
pattern = r'abc'
string = r'dabc'
# match_object = re.search(pattern, string)
# print('match_object=', match_object)
#
# pattern = r'a[a-zA-Z]c'  # любая буква
# string = r'abc'
# match_object = re.match(pattern, string)
# print('match_object= ', match_object)
#
# string = 'abc, acc, bbc'
# all_inclusions = re.findall(pattern, string)
# print('all_inclusions= ', all_inclusions)
#
# fixed_typos = re.sub(pattern, 'abc', string)
# print('fixed_typos= ', fixed_typos)
#
# #example with interrogatory(?)
# pattern = r'english\?'
# string = r'Do you speak english?'
# match_object = re.search(pattern, string)
# print('match_object= ', match_object)
#
#
# #example with ( )
# pattern = r'(test|text)*'
# string = r'testtext'
# test = re.match(pattern, string)
# print('test= ', test)
#
# #example with groups
# pattern = r'Hello (abc|test)'
# string = r'Hello abc'
# test = re.match(pattern, string)
# print('test= ', test)
# print(test.group())    # 0 задан аргументом по умолчанию
#
# #example with groups
# pattern = r'(\w*)-\1'    # \1 - номер группы
# string = r'test-test'
# test = re.match(pattern, string)
# print('test= ', test)
# print(test.group())    # 0 задан аргументом по умолчанию
#
# x = (re.match(r'text', 'TEXT', re.IGNORECASE))
# print('x= ', x)


import sys
sys.stdin = open("input.txt", "r")
pattern = 'cat'


def first():
    for line in sys.stdin:
        line = line.rstrip()
        sear = re.findall(pattern, line)
        if len(sear) > 1:
            print(line)
#first()


def second():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'\bcat\b'
        x = re.findall(pattern, line)
        if x:
            print(line)
# second()


def third():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'z[a-zA-Z]{3}z'   # [a-zA-Z]{2} means two letters
        x = re.search(pattern, line)
        if x:
            print(line)

# third()


def forth():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'\\'
        x = re.search(pattern, line)
        if x:
            print(line)

#forth()

def fifth():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r"\b(\w+)\1\b"
        x = re.search(pattern, line)
        if x:
            print(line)

# fifth()


def sixth():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r"human"
        line = re.sub(pattern, 'computer', line)
        print(line)

# sixth()


def seventh():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'\ba+\b'    # world contained only charter a
        line = re.sub(pattern, 'argh', line, 1, re.IGNORECASE)
        print(line)

#seventh()


def eighth():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'\b(\w)(\w)'  # get the first two letters in words
        line = re.sub(pattern, r'\2\1', line)  # swap letters
        print(line)

#eighth()

def ninth():
    for line in sys.stdin:
        line = line.rstrip()
        pattern = r'(.)\1{1,}'  # matches one or more characters from 1st group
        line = re.sub(pattern, r'\1', line)  #
        print(line)

ninth()
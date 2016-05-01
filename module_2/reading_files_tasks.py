import os

def record_revers(file1, file2):
    """
    считываем файл и записываем информацию в другой в обратном порядке
    """
    with open(file1) as f, open(file2, 'a') as w:
        for line in reversed(list(f)):
            if line[-1:] != '\n':
                line += '\n'
            #w.seek(0)
            print(repr(line))
            w.write(line)

#record_revers('test.txt', 'answ.txt')

def find_py(folder):
    """
    функция имет файлы .py в указанной папке и глубже и возвращает пути где они лежат
    """
    answ = []
    for current_dir, dirs, files in os.walk(folder):
        #print(current_dir, dirs, files)
        for file in files:
            if file.endswith('.py') and current_dir not in answ:
                answ.append(current_dir)
    return answ

#print(find_py('sample'))
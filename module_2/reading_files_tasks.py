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


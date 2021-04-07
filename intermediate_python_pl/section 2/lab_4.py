import os

path = r"lab_4.txt"


def count_words(path):
    file = open(path).read()
    file = file.split(' ')
    return len(file)


if os.path.isfile(path):
    words = count_words(path)
    print(f'file {path} exist and has {words} words')
else:
    print('file does not exist')


os.path.isfile(path) and print(f'file {path} exist and has {count_words(path)} words')

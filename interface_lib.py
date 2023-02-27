import os


def clear_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def print_element(elmt):
    print(f"Имя: {elmt[0]}, {elmt[1]} {elmt[2]}")
    print(f"Тел: {'  '.join(elmt[3])}")
    print(f"e-mail: {'  '.join(elmt[4])}")
    print(f"addr: {elmt[5]}")
    print()


def print_book(data):
    for k, v in data.items():
        print(f"#{k}")
        print_element(v)
        # print(f"Имя: {v[0]}, {v[1]} {v[2]}")
        # print(f"Тел: {'  '.join(v[3])}")
        # print(f"e-mail: {'  '.join(v[4])}")


def find_element(data, element):
    not_found = True
    for k, v in data.items():
        if element in v:
            print_element(v)
    if not_found:
        print('Ничего не нашёл')

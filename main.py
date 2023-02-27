import JSON_format as jsons
import interface_lib as iface

# Data structure {id: ['l_name', 'f_name', 'm_name', ['phone'], ['email'], 'city']}

phonebook = jsons.load('PD_DB.json')
# del phonebook['id']
print(f"Количество записей: {len(phonebook)}")
print(max(phonebook.keys()))

flag = True
while flag:
    # iface.clear_screen()
    print('Доступные опции:', \
          '1 -> вывести все контакты', \
          '2 -> добавление контакта', \
          '3 -> поиск контакта', \
          '4 -> изменить контакт', \
          '5 -> удалить контакт', \
          '0 -> выход (с сохранением)', \
          sep='\n')

    user_input = input('> ').lower()
    match user_input:
        case "1":
            print('Отображение списка.')
            iface.print_book(phonebook)
        case "2":
            print('Добавление контакта')
            # блок ВВОДА
            next_id = int(max(phonebook.keys())) + 1
            ph_record = input('Введите ФИО через пробел (порядок важен): ').split()
            if len(ph_record) < 3:
                for i in range(3 - len(ph_record)):
                    ph_record.append('')
            ph_record.append(
                input('Введите номера телефонов через пробел (в самом номере не должно быть пробелов): ').split())
            ph_record.append(
                input('Введите email адреса через пробел: ').split())
            ph_record.append(input('Введите адрес: '))
            print(ph_record)
            phonebook[next_id] = ph_record
        case "3":
            print('Поиск контакта')
            print(
                'Поиск проводится по любому полю справочника, по полному или частичному совпадению (Чувствительно к регистру). '
                'Задайте строку поиска. Если хотите найти по номеру записи, введите #n (n - номер записи).')
            string_to_find = input('> ')
            if string_to_find.startswith('#'):
                iface.print_element(phonebook[string_to_find[1:]])
            else:
                iface.find_element(phonebook, string_to_find)
        case "4":
            print('Изменить контакт')
            # Change entry here
            # string_to_find = input('Что ищем? ')
            # iface.find_element(phonebook, string_to_find)
        case "5":
            print('Удалить контакт')
            # Delete entry here
            # string_to_find = input('Что ищем? ')
            # iface.find_element(phonebook, string_to_find)
        case "0":
            print('quiting')
            jsons.save('PD_DB.json', phonebook)
            flag = False

import os
import JSON_format as jsons
import interface_lib as iface

# Data structure
# phonebook = {id: [l_name, f_name, m_name, [phone1, phone2], [email1, email2], address]}
#phonebook = {1: ['Smith', 'John', None, ['+1776849096'], ['abc@d.com']]}
phonebook = jsons.load('PB_DB.json')
print(phonebook)
jsons.save('PD_DB.json', phonebook)
# phonebook = [
#  [12345, True, "яблоко", {"Миша": [898981646, 464654654]}],\
#  [12345, True, "яблоко", {"Миша": [898981646, 464654654]}]\
#  ]
#print(*phonebook)
#jsons.write_json_file('PB_DB.json', phonebook)
1
# phonebook = jsons.load('PB_DB.json')
# print(phonebook)
#
# pb_record = {'surname': "Иванов", 'firstname': 'Иван', 'middlename': 'Иванович', 'address': '', 'email': [], 'phone': []\
#              }


# read from file here
flag = True
while flag:
    iface.clear_screen()
    #os.system('clear')
    print('Доступные опции:',\
          '1 -> выводит список на экран',\
          '2 -> добавление контакта',\
          '3 -> поиск контакта',\
          '0 -> выход (с сохранением)',\
          sep='\n')

    user_input = input('> ').lower()
    match user_input:
        case "1":
            print('Отображение списка.')
        case "2":
            print('Добавление контакта')
            # блок ВВОДА
        case "3":
            print('Поиск контакта')
        case "0":
            print('quiting')
            # save to file here
            flag = False

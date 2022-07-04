import sys
import os


address_1 = os.path.abspath('less_6_users.csv')
address_2 = os.path.abspath('less_6_hobby.csv')
address_3 = os.path.abspath('lesson_6_dict.txt')


comand = sys.argv


address_input = input('Введите адрес первого файла: ')
if address_input == address_1:
    # sys.argv[0] = address_input
    address_1_input = input('Введите адрес второго файла: ')
    # sys.argv[1] = address_1_input
    if address_1_input == address_2:
        address_3_input = input('Введите адрес третьего файла: ')
        # sys.argv[2] = address_3_input
        if address_3_input == address_3:
            with open('less_6_users.csv', 'r', encoding='utf-8') as fus:
                users = fus.read()
                print('less_6_users.csv', users, end='\n')
            with open('less_6_hobby.csv', 'r', encoding='utf-8') as fhu:
                hobby = fhu.read()
                print('less_6_hobby.csv', hobby, end='\n')
            with open('lesson_6_dict.txt', 'r', encoding='utf-8') as fd:
                f_dict = fd.read()
                print('lesson_6_dict.txt', f_dict, end='\n')
        else:
            print('Вы ввели неверный путь к файлу')


    else:
        print('Вы ввели неверный путь к файлу')

else:
    print('Вы ввели неверный путь к файлу')
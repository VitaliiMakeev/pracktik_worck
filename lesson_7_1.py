import os
import sys
import glob
import shutil


def sam_in(f_path):
    """Функция просмотра файлов и папок в дерриктории f_path"""
    if os.path.exists(f_path):
        print(f'Тут {f_path}, \nТакие файлы и папки\n{os.listdir(f_path)}')

    else:
        print(f'В этой дерриктории\n{f_path}\nтакой папки нет.')

tmp = []
my_list = []
my_list_level_2 = []
my_list_level_3 = []
my_list_app = []
my_list_app_leve_2 = []

# Распарсиваю confing.yaml

with open('confing.yaml', 'r', encoding='utf-8') as f:
    fbr = f.read().split('\n')
    for i in fbr:
        n = len(i) - i.count(' ')
        k = len(i) - n
        if '.' not in i and k <= 2:
            n = i.replace(' ', '')
            nn = n.replace(':', '')
            my_list.append(nn)
        elif '.' not in i and k == 4:
            n = i.replace(' ', '')
            nn = n.replace(':', '')
            my_list_level_2.append(nn)
        elif '.' not in i and k == 6:
            n = i.replace(' ', '')
            nn = n.replace(':', '')
            my_list_level_3.append(nn)
        elif '.' in i and k == 4:
            n = i.replace(' ', '')
            my_list_app.append(n)
            if my_list_app.count(n) > 1:
                my_list_app.remove(n)
        else:
            n = i.replace(' ', '')
            my_list_app_leve_2.append(n)
            if my_list_app_leve_2.count(n) > 1:
                my_list_app_leve_2.remove(n)




# print(my_list)
# print(my_list_level_2)
# print(my_list_level_3)
# print(my_list_app)
# print(my_list_app_leve_2)


comand = sys.argv
BASE_PATH = os.getcwd()
# print(BASE_PATH)

new_project = os.path.join(BASE_PATH, my_list[0])

if comand[1] == 'start':
    if not os.path.exists(new_project):
        os.mkdir(my_list[0])
        os.chdir(my_list[0])
        old_path = os.path.join(BASE_PATH, my_list[0])
        for i in my_list[1:]:
            os.mkdir(i)
        os.chdir(my_list[4])
        q = open(my_list_app[2], 'x', encoding='utf-8')
        q.close()
        w = open(my_list_app[3], 'x', encoding='utf-8')
        w.close()
        e = open(my_list_app[4], 'x', encoding='utf-8')
        e.close()
        os.chdir(old_path)
        os.chdir(my_list[3])
        t = open(my_list_app[2], 'x', encoding='utf-8')
        t.close()
        y = open(my_list_app[0], 'x', encoding='utf-8')
        y.close()
        u = open(my_list_app[1], 'x', encoding='utf-8')
        u.close()
        os.mkdir(my_list_level_2[0])
        os.chdir(my_list_level_2[0])
        os.mkdir(my_list_level_3[1])
        os.chdir(my_list_level_3[1])
        a = open(my_list_app_leve_2[0], 'x', encoding='utf-8')
        a.close()
        s = open(my_list_app_leve_2[1], 'x', encoding='utf-8')
        s.close()
        os.chdir(old_path)
        os.chdir(my_list[2])
        d = open(my_list_app[2], 'x', encoding='utf-8')
        d.close()
        f = open(my_list_app[0], 'x', encoding='utf-8')
        f.close()
        g = open(my_list_app[1], 'x', encoding='utf-8')
        g.close()
        os.mkdir(my_list_level_2[0])
        os.chdir(my_list_level_2[0])
        os.mkdir(my_list_level_3[0])
        os.chdir(my_list_level_3[0])
        h = open(my_list_app_leve_2[0], 'x', encoding='utf-8')
        h.close()
        j = open(my_list_app_leve_2[1], 'x', encoding='utf-8')
        j.close()
    elif os.path.exists(my_list[0]):
        print('Такая папка уже есть.', os.path.dirname(os.path.abspath(my_list[0])))
        new_name = input('Введите другое имя нового проекта: ')
        new_project_1 = os.path.join(BASE_PATH, new_name)
        if not os.path.exists(new_project_1):
            os.mkdir(new_name)
            os.chdir(new_name)
            old_path_1 = os.path.join(BASE_PATH, new_name)
            for i in my_list:
                os.mkdir(i)
            os.chdir('setting')
            q = open(my_list_app[2], 'x', encoding='utf-8')
            q.close()
            w = open(my_list_app[3], 'x', encoding='utf-8')
            w.close()
            e = open(my_list_app[4], 'x', encoding='utf-8')
            e.close()
            os.chdir(old_path)
            os.chdir(my_list[3])
            t = open(my_list_app[2], 'x', encoding='utf-8')
            t.close()
            y = open(my_list_app[0], 'x', encoding='utf-8')
            y.close()
            u = open(my_list_app[1], 'x', encoding='utf-8')
            u.close()
            os.mkdir(my_list_level_2[0])
            os.chdir(my_list_level_2[0])
            os.mkdir(my_list_level_3[0])
            os.chdir(my_list_level_3[0])
            a = open(my_list_app_leve_2[0], 'x', encoding='utf-8')
            a.close()
            s = open(my_list_app_leve_2[1], 'x', encoding='utf-8')
            s.close()
            os.chdir(old_path)
            os.chdir(my_list[2])
            d = open(my_list_app[2], 'x', encoding='utf-8')
            d.close()
            f = open(my_list_app[0], 'x', encoding='utf-8')
            f.close()
            g = open(my_list_app[1], 'x', encoding='utf-8')
            g.close()
            os.mkdir(my_list_level_2[0])
            os.chdir(my_list_level_2[0])
            os.mkdir(my_list_level_3[0])
            os.chdir(my_list_level_3[0])
            h = open(my_list_app_leve_2[0], 'x', encoding='utf-8')
            h.close()
            j = open(my_list_app_leve_2[1], 'x', encoding='utf-8')
            j.close()
        else:
            print('Что то опять не так сделали, начните заново.')
elif comand[1] == 'rename':
    name_path = input('Введите название папки для смены ее имени: ')
    new_name_path = input('Введите новое имя папки: ')
    if os.path.exists(name_path) and not os.path.exists(new_name_path):
        os.rename(name_path, new_name_path)
    elif not os.path.exists(name_path):
        print(name_path, 'Такой папки нет.')
    elif os.path.exists(new_name_path):
        print(os.path.dirname(os.path.abspath(new_name_path)), 'Такая папка уже есть, введите другое имя новой папки.')

elif comand[1] == 'el':
    sam_in(comand[2])
elif comand[1] == 'copy':
    os.chdir('my_project')
    if not os.path.exists('./templates'):
        os.mkdir('./templates')
    temp = './templates/'
    for file in glob.glob("**/templates/**/*.html"):
        qq = file.split('/')
        for i in qq:
            ww = i.split('\\')
            new_file = temp + ww[2] + '/' + ww[3]
            new_path = temp + ww[2]
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            fp = open(new_file, 'w')
            fp.close()
            shutil.copyfile(file, new_file)
elif comand[1] == 'summa':
    dict_1 = {}
    list_1 = []
    list_1_1 = []
    list_2 = []
    list_2_2 = []
    list_3 = []
    list_3_3 = []
    list_4 = []
    list_4_4 = []
    list_5 = []
    list_5_5 = []
    list_6 = []
    list_6_6 = []

    for q, w, e in os.walk(os.getcwd()):
        for j in e:
            path_11 = q + '/' + j
            file_path, file = os.path.splitext(path_11)
            path_22 = file_path + '/' + file
            file_siz = os.stat(path_11).st_size
            if file_siz <= 100:
                list_1.append(j)
                list_1_1.append(file)
                dict_1[100] = (len(list_1), list_1_1)
            elif 100 < file_siz <= 1000:
                list_2.append(j)
                list_2_2.append(file)
                dict_1[1000] = (len(list_2), list_2_2)
            elif 1000 < file_siz <= 10000:
                list_3.append(j)
                list_3_3.append(file)
                dict_1[10000] = (len(list_3), list_3_3)
            elif 10000 < file_siz <= 100000:
                list_4.append(j)
                list_4_4.append(file)
                dict_1[100000] = (len(list_4), list_4_4)
            elif 100000 < file_siz <= 1000000:
                list_5.append(j)
                list_5_5.append(file)
                dict_1[1000000] = (len(list_5), list_5_5)
            elif 1000000 < file_siz <= 10000000:
                list_6.append(j)
                list_6_6.append(file)
                dict_1[10000000] = (len(list_6), list_6_6)
    dict_1_1 = sorted(dict_1.items())
    dict_final = dict(dict_1_1)
    # print(dict_final)

    fff = os.getcwd()
    fol = fff.split('/')
    folder = None
    for i in fol:
        folder = i.split('\\')[-1]
    name_file = folder + '_summary.json'
    with open(name_file, 'w', encoding='utf-8') as fa:
        fa.write('{\n')
        fa.seek(2)
        for key, val in dict_final.items():
            res = f'  {key}: {val}'
            result = f'{res}\n'
            fa.write(result)
        fa.seek(0, 2)
        fa.write('}')
elif comand[1] == 'help':
    print('start - создание новой заготовки (my_project - по умолчанию)\n'
          'rename - переименование дерриктории,\n '
          'el - просмотр содержимого дерриктории,\n'
          'copy - копирование папок с файлами *.html в одну папку "templates",\n'
          'summa - выводит статистику в файле <имя папки>_summary.json')
else:
    print('Неверная команда, введите - help')




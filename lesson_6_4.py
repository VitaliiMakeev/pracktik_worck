

with open('less_6_users.csv', 'r', encoding='utf-8') as fus:
    users =  fus.read()
    users_list = users.splitlines()

    users_list_tmp = [i.split(',') for i in users_list]


    dict_user = {}
    soname_list = []
    name_list = []
    patronymic_list = []

    for soname in users_list_tmp:
        soname_list.append(soname[0])
        name_list.append(soname[1])
        patronymic_list.append(soname[2])
        dict_user['soname'] = soname_list
        dict_user['name'] = name_list
        dict_user['patronymic'] = patronymic_list



    with open('less_6_hobby.csv', 'r', encoding='utf-8') as fho:
        hobby = fho.read()
        hobby_list = hobby.splitlines()
        dict_user['hobby'] = hobby_list

    with open('lesson_6_dict.txt', 'r', encoding='utf-8') as fd:
        dict_1 = fd.read()
        dict_2 = dict_1.split(', ')
        dict_2[0] = dict_2[0].replace('{', '').replace("'", "")
        dict_2[1] = dict_2[1].replace("'", "")
        dict_2[-1] = dict_2[-1].replace('}', '').replace("'", "")

        dict_user['name_hobby'] = dict_2
        print(dict_user)

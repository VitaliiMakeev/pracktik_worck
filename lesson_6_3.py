from itertools import zip_longest

# name = ['Иванов,Иван,Иванович', 'Петров,Петр,Петрович', 'Кузьмин,Кузьма,Валерьевич']
# hobby = "поедание сосисок\nзаплетение косичек\nпрогулки в парке"
#
# with open('less_6_users.csv', 'w', encoding='utf-8') as fn:
#     for i in name:
#         fn.write(i + '\n')
#
# with open('less_6_hobby.csv', 'w', encoding='utf-8') as fhob:
#         fhob.write(hobby)

with open('less_6_users.csv', 'r', encoding='utf-8') as fn:
    user = fn.read()
    user_list = user.splitlines()
    # print(user_list)

    with open('less_6_hobby.csv', 'r', encoding='utf-8') as fhob:
        hobby_1 = fhob.read()
        hobby_list = hobby_1.splitlines()
        # print(hobby_list)
        if len(user_list) >= len(hobby_list):
            dict_file = dict(zip_longest(user_list, hobby_list))
            print(dict_file)
        else:
            print('1')
        with open('lesson_6_dict.txt', 'w', encoding='utf-8') as fr:
            fr.write(str(dict_file))


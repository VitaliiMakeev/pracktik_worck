from collections import Counter
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    new_list = []
    new_api_list = []
    for i in content:
        new_list.append(i.strip())
    for n in new_list:
        jast_1 = n.split(',')
        jast_1_1 = jast_1[0].replace('(', '').replace("'", "")
        new_api_list.append(jast_1_1)
    spam_serch = dict(Counter(new_api_list))
    sorted_valios = sorted(spam_serch.values())
    sorted_dict_spam = {}
    for i in sorted_valios:
        for k in spam_serch.keys():
            if spam_serch[k] == i:
                sorted_dict_spam[k] = spam_serch[k]
    last_val_spam = reversed(sorted_dict_spam.values())
    last_key_spam = reversed(sorted_dict_spam.keys())
    print(next(last_val_spam), next(last_key_spam))



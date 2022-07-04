import re
import sys



# Задания 6 и 7



comand = sys.argv


if len(comand) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        fb = f.read()
        print(fb)
if len(comand) == 2:
    if '.' in comand[1]:
        fred = f'{comand[1]}''\n'
        with open('bakery.csv', 'a', encoding='utf-8') as faaar:
            faaar.write(fred)

        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            read_1 = fr.read()
            read_2 = read_1.splitlines()
            sum_numbers = []
            for i in read_2:
                num = float(i)
                sum_numbers.append(num)
            print(sum(sum_numbers))
    else:
        with open('bakery.csv', 'r', encoding='utf-8') as dr:
            dro = dr.read()
            drop = dro.splitlines()
            index = int(comand[1])
            for n in drop[index - 1:]:
                print(n)
elif len(comand) == 3:
    if '.' not in comand[1]:
        with open('bakery.csv', 'r', encoding='utf-8') as fl:
            flo = fl.read()
            flop = flo.splitlines()
            index_1 = int(comand[1])
            index_2 = int(comand[2])
            for ind in flop[index_1 - 1: index_2]:
                print(ind)

    elif '.' in comand[1]:
        with open('bakery.csv', 'r+', encoding='utf-8') as ch:
            che = ch.read()
            che = re.sub(comand[1], comand[2], che)
            ch.seek(0)
            ch.write(che)
            ch.truncate()





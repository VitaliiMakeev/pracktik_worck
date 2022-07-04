tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

for i in range(len(tutors) - len(klasses)):
    klasses.append(None)

tut_klass = (j for j in list(zip(tutors, klasses)))

print(next(tut_klass))
print(next(tut_klass))
print(next(tut_klass))
print(next(tut_klass))
print(next(tut_klass))
print(next(tut_klass))
print(next(tut_klass))




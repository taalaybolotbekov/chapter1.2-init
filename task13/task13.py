apple = int(input('Введите количество яблок: '))
students = int(input('Введите количество учеников: '))
apple1 = 0
if apple == students:
    print('раздали студентам: ', apple % students)
elif apple > students:
    apple1 += 1
    print('раздали студентам: ', apple % students, 'Остаток яблок: ', apple1)
else:
    print('цифрами')
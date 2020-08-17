user = int(input('Введите возраст собаки: '))
doggy = input('Введите размер собаки: ')
if doggy == 'маленький':
    print(user*9)
elif doggy == 'средний':
    print(user*10.5)
elif doggy == 'большой':
    print(user*12.5)
else:
    print('error')
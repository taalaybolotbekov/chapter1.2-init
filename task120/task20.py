user1 = int(input('Введите первое число: '))
user2 = int(input('Введите второе число: '))
user3 = int(input('Введите третее число: '))
if user1 > user2 and user1 < user3 or user1 > user3 and user1 < user2:
    print('первое число средняя')
elif user2 > user1 and user2 < user3  or user2 < user1 and user2 > user3:
    print('второе число средняя')
elif user3 > user1 and user3 < user2 or user3 < user1 and user3 > user2:
    print('третье число средняя')
else:
    print('все одинаковые')
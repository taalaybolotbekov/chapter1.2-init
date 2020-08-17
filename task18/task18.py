num = int(input('Введите число: '))
step = int(input('Введите степень: '))
if num < 100:
    result = num ** step
    print(result)
else:
    print('Число больше 100')
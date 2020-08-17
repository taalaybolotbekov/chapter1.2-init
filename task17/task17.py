a = int(input('введите первую: '))
b = int(input('введите вторую: '))
c = int(input('введите третью: '))
d = [a, b, c]
e = 0
for i in range(3):
    if d[i] > 0:
        e += 1
print('Количество положительных чисел: ', e)
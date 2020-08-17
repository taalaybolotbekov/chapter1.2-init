a = int(input('введите первую: '))
b = int(input('введите вторую: '))
c = int(input('введите третью: '))
m = a
if b > c:
    m = b
elif c > a:
    m = c
print('Max ', m)

# d = [a, b, c]
# m = 0
# for i in d:
#     if a > b:
#         m += 1
#     elif a < b:
#         m += 1
#     elif a > c:
#         m += 1
#     elif a < c:
#         m += 1
#     elif b > c:
#         m += 1
#     elif b < c:
#         m += 1
#     else:
#         print('error')
# print(m)
# # print('Количество положительных чисел: ', m)
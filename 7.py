from random import randint
def pr_delta(sp, min_sp, delta):
    fl = 0
    if sp - min_sp == delta:
        fl = 1
    return fl
delta = int(input('Введите значение Delta:'))
n = int(input('Введите число элементов последовательности: '))
if n == 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
else:
    sp = [0] * n
    print('Введите', n, 'элементов или нажмите Enter для случайной генерации элемента')
    for i in range(n):
        sp[i] = input()
        if sp[i] == '':
            sp[i] = int(randint(1, 100))
        else:
            sp[i] = int(sp[i])
print(sp)
count = 0
for i in range(n):
    if pr_delta(sp[i], min(sp), delta) == 1:
        count += 1
print(count)


from random import randint
n = input('введите число элементов 1 последовательности ')
a = '0123456789'
b = ''
for elem in n:
    for nomer in a:
        if elem == nomer:
            b += elem
if len(b) == 0:
    print('Ошибка. Вы ввели не число')
    sp1 = []
elif int(n) <= 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
    sp1 = []
else:
    n = int(n)
    sp1 = [0] * n
    print('введите', n, 'элементов или нажмите Enter для случайной генерации элемента')
    for i in range(n):
        sp1[i] = input()
        if sp1[i] == '':
            sp1[i] = int(randint(-100, 100))
        else:
            sp1[i] = int(sp1[i])
    print('Элементы первой последовательности', sp1)
m = input('введите число элементов 2 последовательности ')
a = '0123456789'
c = ''
for elem in m:
    for nomer in a:
        if elem == nomer:
            c += elem
if len(c) == 0:
    print('Ошибка. Вы ввели не число')
    sp2 = []
elif int(m) <= 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
    sp2 = []
else:
    m = int(m)
    sp2 = [0] * m
    print('введите', m, 'элементов или нажмите Enter для случайной генерации элемента')
    for i in range(m):
        sp2[i] = input()
        if sp2[i] == '':
            sp2[i] = int(randint(-100, 100))
        else:
            sp2[i] = int(sp2[i])
    print('Элементы второй последовательности', sp2)
if len(sp1) > 0 and len(sp2) > 0:
    sp3 = []
    print('Общие элементы для 1 и 2 последовательностей:')
    for item in sp1:
        if item in sp2 and item not in sp3:
            sp3.append(item)
    for item in sp3:
        if sp1.count(item) > sp3.count(item) and sp2.count(item) > sp3.count(item):
            min_zn = min(sp1.count(item), sp2.count(item))
            for i in range(min_zn - 1):
                sp3.append(item)
    for i in range(len(sp3)):
        print(sp3[i])

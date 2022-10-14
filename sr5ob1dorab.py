from random import randint
n = input('введите число элементов последовательности ')
a = '0123456789'
b = ''
for elem in n:
    for nomer in a:
        if elem == nomer:
            b += elem
print(b)
if len(b) == 0:
    print('Ошибка. Вы ввели букву')
elif int(n) <= 0:
    print('Ошибка. Число элементов последовательности должно быть больше 0')
else:
    n = int(n)
    sp = [0] * n
    print('введите', n, 'чисел или нажмите Enter для случайной генерации элемента')
    for i in range(n):
        sp[i] = input()
        if sp[i] == '':
            sp[i] = float(randint(-100, 100))
        else:
            sp[i] = float(sp[i])
    print(sp)
    maxElem = 1 * 10 ** -10
    nommax = 0
    for i in range(n):
        if sp[i] > maxElem:
            maxElem = sp[i]
            nommax = i
    for i in range(nommax + 1, n):
        sp[i] = 0
    print(sp)

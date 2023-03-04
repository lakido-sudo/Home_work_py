'''
Задача 26:
'''

A = int(input('Введите А: '))
B = int(input('Введите B: '))


def stepen(A):
    if A == 1:
        return 1
    elif B == 0:
        return 1
    else:
        return A**B


print(stepen(A))

'''
Задача  28
'''

a = int(input('Введи целое не отр. число 1: '))
b = int(input('Введи целое не отр. число 2: '))

    
if a < 0 or b < 0:
    print('Введите положительные')
else:
    def summa(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return int(a) + int(b)
    print(summa(a, b))

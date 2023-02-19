'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''
print('Задача 2')

num = str(123)
print(sum(map(int, num)))

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.

Вместе они сделали S журавликов. Сколько журавликов сделал

каждый ребенок, если известно, что Петя и Сережа сделали

одинаковое количество журавликов, а Катя сделала в два раза

больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''

print('Задача 4')

# S = sum_of_shadoof

sum_of_shadoof = 11

x = sum_of_shadoof/6

shadoof_by_Piter = x
shadoof_by_Serg = x
shadoof_by_Kate = (x + x) * 2

print(round(shadoof_by_Piter, 1))
print(round(shadoof_by_Serg, 1))
print(round(shadoof_by_Kate, 1))

'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно,

вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером,

где сумма первых трех цифр равна сумме последних трех. Т.е.
билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''

print('Задача 6')

n = str(123321)
print('Yes' if sum(map(ord, n[:3])) == sum(map(ord, n[3:])) else 'Yes')

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n x m

долек отломить k долек, если разрешается сделать один разлом по прямой

между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

print('Задача 8')

n = 2
m = 3

k = int(input())

print('Yes' if k < n * m else 'No')

# Рекурсия. А в степени В

A = int(input("Введите число A: "))
B = int(input("Введите его степень B: "))


def stepen(A, B):
    if B == 1:
        return A
    elif B == 0:
        return 1
    if B != 1:
        return A * stepen(A, B - 1)


print("Результат возведения в степень равен: ", stepen(A, B))

# Рекурсия. sum(a, b)

a = int(input('Введите а: '))
b = int(input('Введите b: '))


def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)


print(summa(a, b))

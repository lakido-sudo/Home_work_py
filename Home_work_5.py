# Рекурсия. А в степени В

A = int(input("Введите число A: "))
B = int(input("Введите его степень B: "))


def stepen(A, B):
    if (B == 1):
        return (A)
    elif (B == 0):
        return 1
    if (B != 1):
        return (A * stepen(A, B - 1))


print("Результат возведения в степень равен: ", stepen(A, B))

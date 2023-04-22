a = int(input("Введите первое неотрицительное число А "))
b = int(input("Введите второе неотрицательно число В "))


def recurs_summa(a, b):
    if a == 0:
        return b
    else:
        return recurs_summa(a - 1, b + 1)


print(f"Сумма чисел {a} и {b} = {recurs_summa(a, b)}")

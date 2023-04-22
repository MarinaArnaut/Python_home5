a = int(input("Введите число А "))
b = int(input("Введите число В "))


def degree_my(a, b):
    if b == 0:
        return 1
    return a * degree_my(a, b - 1)


print(f"Число {a} в степени {b} равно {degree_my(a, b)}")

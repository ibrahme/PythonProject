# Ввод двух чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Сравнение чисел
if a > b:
    print(f"Наибольшее число: {a}")
elif b > a:
    print(f"Наибольшее число: {b}")
else:
    print("Оба числа равны.")

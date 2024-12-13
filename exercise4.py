# Ввод чисел A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Проверка условия A <= B
if A > B:
    print("Ошибка: A должно быть меньше или равно B.")
else:
    # Вывод чисел от A до B
    for num in range(A, B + 1):
        print(num, end=" ")

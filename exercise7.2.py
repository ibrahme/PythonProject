# Функция для вычисления суммы и среднего арифметического массива
def calculate_sum_and_average(array):
    total = sum(array)  # Сумма элементов
    average = total / len(array) if array else 0  # Среднее арифметическое
    return total, average

# Основная программа
def main():
    # Ввод массивов
    array1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
    array2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))
    array3 = list(map(int, input("Введите элементы третьего массива через пробел: ").split()))

    # Проверка на ограничение размера массива
    if len(array1) > 15 or len(array2) > 15 or len(array3) > 15:
        print("Ошибка: размер массива не должен превышать 15 элементов.")
        return

    # Вычисление суммы и среднего арифметического для каждого массива
    total1, avg1 = calculate_sum_and_average(array1)
    total2, avg2 = calculate_sum_and_average(array2)
    total3, avg3 = calculate_sum_and_average(array3)

    # Вывод результатов
    print(f"Массив 1: сумма = {total1}, среднее = {avg1:.2f}")
    print(f"Массив 2: сумма = {total2}, среднее = {avg2:.2f}")
    print(f"Массив 3: сумма = {total3}, среднее = {avg3:.2f}")

# Запуск программы
main()

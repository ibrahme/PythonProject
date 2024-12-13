def main():
    # Ввод размера матрицы
    n = int(input("Введите размер матрицы (N): "))
    if n <= 0:
        print("Ошибка: размер матрицы должен быть больше 0.")
        return

    # Ввод матрицы
    print("Введите элементы матрицы построчно, через пробел:")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Ошибка: количество элементов в строке должно быть равно N.")
            return
        matrix.append(row)

    # Инициализация суммы и счётчика положительных элементов
    positive_sum = 0
    positive_count = 0

    # Проход по элементам над главной диагональю
    for i in range(n):
        for j in range(i + 1, n):  # Над главной диагональю: j > i
            if matrix[i][j] > 0:
                positive_sum += matrix[i][j]
                positive_count += 1

    # Вывод результатов
    print(f"Сумма положительных элементов над главной диагональю: {positive_sum}")
    print(f"Число положительных элементов над главной диагональю: {positive_count}")

# Запуск программы
main()

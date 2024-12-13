def main():
    # Ввод размеров матрицы
    n = int(input("Введите количество строк (N): "))
    m = int(input("Введите количество столбцов (M): "))
    if n <= 0 or m <= 0:
        print("Ошибка: размеры матрицы должны быть положительными числами.")
        return

    # Ввод матрицы
    print("Введите элементы матрицы построчно, через пробел:")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print("Ошибка: количество элементов в строке должно быть равно M.")
            return
        matrix.append(row)

    # Обработка строк матрицы
    for i in range(n):
        row = matrix[i]
        max_value = max(row)
        min_value = min(row)
        max_index = row.index(max_value)
        min_index = row.index(min_value)

        # Замена максимального элемента с первым
        row[0], row[max_index] = row[max_index], row[0]

        # Замена минимального элемента с последним
        row[-1], row[min_index] = row[min_index], row[-1]

        # Обновление строки в матрице
        matrix[i] = row

    # Вывод результата
    print("Обработанная матрица:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Запуск программы
main()

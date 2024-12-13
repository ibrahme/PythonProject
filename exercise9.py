def factorial(n):
    """
    Рекурсивная функция для вычисления факториала числа n.
    
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(x, n):
    """
    Рекурсивная функция для вычисления x^n.

    """
    if n == 0:
        return 1
    return x * power(x, n - 1)

def compute_expression(x, n):
    """
    Вычисление выражения x^n / n!.
    """
    return power(x, n) / factorial(n)

# Чтение входных данных
x = int(input("Введите значение X: "))
n = int(input("Введите значение N: "))

# Вычисление и вывод результата
result = compute_expression(x, n)
print(f"Результат выражения {x}^{n} / {n}! равен: {result}")

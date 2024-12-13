import math

def calculate_area():
    print("Выберите фигуру для вычисления площади:")
    print("1. Квадрат")
    print("2. Прямоугольник")
    print("3. Круг")
    print("4. Треугольник")
    print("5. Трапеция")

    choice = int(input("Введите номер фигуры: "))

    if choice == 1:
        # Площадь квадрата
        side = float(input("Введите длину стороны квадрата: "))
        area = side ** 2
        print(f"Площадь квадрата: {area}")
    
    elif choice == 2:
        # Площадь прямоугольника
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        area = width * height
        print(f"Площадь прямоугольника: {area}")
    
    elif choice == 3:
        # Площадь круга
        radius = float(input("Введите радиус круга: "))
        area = math.pi * radius ** 2
        print(f"Площадь круга: {area:.2f}")
    
    elif choice == 4:
        # Площадь треугольника
        base = float(input("Введите длину основания треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = 0.5 * base * height
        print(f"Площадь треугольника: {area}")
    
    elif choice == 5:
        # Площадь трапеции
        a = float(input("Введите длину первого основания трапеции: "))
        b = float(input("Введите длину второго основания трапеции: "))
        height = float(input("Введите высоту трапеции: "))
        area = 0.5 * (a + b) * height
        print(f"Площадь трапеции: {area}")
    
    else:
        print("Некорректный выбор. Попробуйте снова.")

# Запуск программы
calculate_area()
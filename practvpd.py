"""Модуль для работы с матрицами (Практическая работа).

Реализует ввод, создание, просмотр матрицы и выполнение заданий 14, 16, 30, 31, 32.
"""

import random


def input_size():
    """Пункт 1. Ввод размера массива."""

    try:
        rows = int(input("Введите количество строк (высота): "))
        cols = int(input("Введите количество столбцов (ширина): "))
        if rows <= 0 or cols <= 0:
            print("Ошибка: Размеры должны быть больше нуля.")
            return 0, 0
        return rows, cols

    except ValueError:
        print("Ошибка: Введите целое число.")
        return 0, 0


def create_array(rows, cols):
    """Пункт 2. Создание массива."""

    if rows == 0 or cols == 0:
        print("Сначала задайте размеры массива (Пункт 1).")
        return None

    print("\n--- Создание массива ---")
    print("1. Вручную")
    print("2. Автоматически (случайные числа от 0 до 100)")
    print("3. Назад")

    choice = input("Выберите вариант: ")
    matrix = []

    if choice == '1':
        print("Введите элементы массива:")
        for i in range(rows):
            row = []
            for j in range(cols):
                while True:
                    try:
                        val = int(input(f"Элемент [{i}][{j}]: "))
                        row.append(val)
                        break
                    except ValueError:
                        print("Ошибка! Введите целое число.")
            matrix.append(row)
        print("Массив успешно создан вручную.")
        return matrix

    if choice == '2':
        matrix = [
            [random.randint(-100, 100) for _ in range(cols)]
            for _ in range(rows)
        ]
        print("Массив успешно заполнен случайными числами.")
        return matrix

    if choice == '3':
        return None

    print("Неверный ввод.")
    return None


def view_array(matrix):
    """Пункт 3. Просмотр созданного массива. """

    if not matrix:
        print("\nМассив пуст или еще не создан.")
        return

    print("\n--- Ваш массив ---")
    for row in matrix:
        print(" ".join(f"{x:4}" for x in row))
    print("-" * 20)


def task_14(matrix):
    """14. Деление всех элементов на максимальный по модулю элемент."""

    if not matrix:
        return

    max_abs = max(abs(x) for row in matrix for x in row)

    if max_abs == 0:
        print("Ошибка: все элементы равны нулю, деление невозможно.")
        return

    new_matrix = [[x / max_abs for x in row] for row in matrix]
    print(f"Результат (максимальный по модулю = {max_abs}):")

    for row in new_matrix:
        print(" ".join(f"{x:7.3f}" for x in row))  # точность до 3 знаков


def task_16(matrix):
    """16. Номера строк, в которых есть хотя бы один элемент, равный 10."""

    if not matrix:
        return

    found_rows = []
    for i, row in enumerate(matrix):
        if 10 in row:
            found_rows.append(i)

    if found_rows:
        print(f"Строки, содержащие число 10 (индексы): {found_rows}")
    else:
        print("Строк с числом 10 не найдено.")


def task_30(matrix):
    """30. Поменять местами элементы симметрично побочной диагонали."""

    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        print("Ошибка: для этой функции матрица должна быть квадратной (N x N).")
        return

    # копия для того чтобы не испортить массив
    res = [row[:] for row in matrix]

    for i in range(rows):
        for j in range(cols):
            if i + j < cols - 1:
                # Меняется местами элемент (i, j) и симметричный ему
                res[i][j], res[cols - 1 - j][rows - 1 - i] = (
                    res[cols - 1 - j][rows - 1 - i],
                    res[i][j],
                )

    print("Матрица после обмена относительно побочной диагонали:")
    for row in res:
        print(" ".join(f"{x:4}" for x in row))


def task_31(matrix):
    """31. Сумма положительных элементов в строках без нулей."""

    if not matrix:
        return

    total_sum = 0
    valid_rows_count = 0

    for row in matrix:
        if 0 not in row:
            valid_rows_count += 1
            total_sum += sum(x for x in row if x > 0)

    if valid_rows_count > 0:
        print(f"Найдено строк без нулей: {valid_rows_count}")
        print(f"Сумма положительных элементов в них: {total_sum}")
    else:
        print("Все строки содержат хотя бы один ноль (или матрица пуста).")


def task_32(matrix):
    """32. Удалить строку и столбец с минимальным элементом."""

    if not matrix:
        return

    # координаты минимального элемента
    min_val = float('inf')
    min_i, min_j = -1, -1

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val < min_val:
                min_val = val
                min_i = i
                min_j = j

    print(f"Минимальный элемент: {min_val} (строка {min_i}, столбец {min_j})")

    new_matrix = []
    for i, row in enumerate(matrix):
        if i == min_i:
            continue
        new_row = []
        for j, val in enumerate(row):
            if j == min_j:
                continue
            new_row.append(val)
        new_matrix.append(new_row)

    print("Матрица после удаления строки и столбца:")
    for row in new_matrix:
        print(" ".join(f"{x:4}" for x in row))


def process_functions(matrix):
    """Пункт 4. Выполнение функций."""

    if not matrix:
        print("\nСначала создайте массив (Пункт 2).")
        return

    while True:
        print("\n--- Выполнение функций ---")
        print("1. [Задание 14] Разделить все элементы на максимальный по модулю")
        print("2. [Задание 16] Найти строки, содержащие число 10")
        print("3. [Задание 30] Обменять элементы относительно побочной диагонали")
        print("4. [Задание 31] Сумма положительных элементов в строках без нулей")
        print("5. [Задание 32] Удалить строку и столбец с минимальным элементом")
        print("0. Назад в главное меню")

        choice = input("Выберите функцию: ")

        if choice == '1':
            task_14(matrix)
        elif choice == '2':
            task_16(matrix)
        elif choice == '3':
            task_30(matrix)
        elif choice == '4':
            task_31(matrix)
        elif choice == '5':
            task_32(matrix)
        elif choice == '0':
            break
        else:
            print("Неверный пункт меню.")


def main():
    """Пункт 5. Главное меню и выход."""

    rows, cols = 0, 0
    matrix = None

    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Ввод размера массива")
        print("2. Создание массива")
        print("3. Просмотр созданного массива")
        print("4. Выполнение функций")
        print("5. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            rows, cols = input_size()
            if rows > 0 and cols > 0:
                print(f"Размеры установлены: {rows} строк, {cols} столбцов.")
                matrix = None
        elif choice == '2':
            matrix = create_array(rows, cols)
        elif choice == '3':
            view_array(matrix)
        elif choice == '4':
            process_functions(matrix)
        elif choice == '5':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Такого пункта нет. Попробуйте снова.")


if __name__ == "__main__":
    main()

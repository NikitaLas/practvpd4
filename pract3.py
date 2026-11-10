"""Модуль для генерации чисел Улама."""

def _check_int(value, arg_name, min_value=1):
    """Проверка value на целое число, которое >= min_value."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(
            f"Аргумент '{arg_name}' должен быть целым числом, "
            f"получено: {type(value).__name__}"
        )
    if value < min_value:
        raise ValueError(
            f"Аргумент '{arg_name}' должен быть >= {min_value}, "
            f"получено: {value}"
        )

def _validate_args(start, stop, limit):
    """Проверка аргументов на целое число и допустимые значения."""
    _check_int(start, "a", min_value=1)
    if stop is not None:
        _check_int(stop, "b", min_value=1)
        if stop <= start:
            raise ValueError(
                f"Аргумент 'b' ({stop}) должен быть больше 'a' ({start})"
            )
    if limit is not None:
        _check_int(limit, "max_count", min_value=1)

def _is_ulam_candidate(candidate, seq, seen):
    """Проверяет, является ли candidate числом Улама."""
    count = 0
    for x in seq:
        y = candidate - x
        if y in seen and y != x and x < y:
            count += 1
            if count > 1:
                return False
    return count == 1

def _next_ulam(seq, seen):
    """Находит следующее число Улама после последнего в seq."""
    candidate = seq[-1] + 1
    while not _is_ulam_candidate(candidate, seq, seen):
        candidate += 1
    return candidate

def ulam_sequence(a=1, b=None, max_count=None):
    """Возвращает список чисел Улама в интервале [a, b)."""
    _validate_args(a, b, max_count)

    result = []
    seq = [1, 2]
    seen = {1, 2}

    for x in seq:
        if x >= a and (b is None or x < b):
            result.append(x)
            if max_count is not None and len(result) >= max_count:
                return result

    while True:
        if b is not None and seq[-1] + seq[-2] >= b:
            return result

        candidate = _next_ulam(seq, seen)

        if b is not None and candidate >= b:
            return result

        seq.append(candidate)
        seen.add(candidate)

        if candidate >= a:
            result.append(candidate)
            if max_count is not None and len(result) >= max_count:
                return result

# примеры работы программы

def example_default_sequence():
    """Пример 1. Числа Улама без ограничений (a=1)."""
    print("Пример 1: первые числа Улама (без ограничений)")
    print(ulam_sequence(a=1, b=50))
    print()

def example_bounded_sequence():
    """Пример 2. Числа Улама в заданном интервале [a, b)."""
    print("Пример 2: числа Улама в интервале [5, 30)")
    print(ulam_sequence(a=5, b=30))
    print()

def example_limited_count():
    """Пример 3. Ограничение количества чисел (max_count)."""
    print("Пример 3: первые 6 чисел Улама (max_count=6)")
    print(ulam_sequence(a=1, b=100, max_count=6))
    print()

def example_type_error():
    """Пример 4. Ошибка типа: передана строка вместо числа."""
    print("Пример 4: демонстрация TypeError")
    try:
        ulam_sequence(a="1")
    except TypeError as error:
        print(f"  TypeError: {error}")
    print()

def example_value_error():
    """Пример 5. Ошибка значения: b меньше или равен a."""
    print("Пример 5: демонстрация ValueError")
    try:
        ulam_sequence(a=10, b=5)
    except ValueError as error:
        print(f"  ValueError: {error}")
    print()

#меню для программы

def _show_menu():
    """Выводит меню на экран."""
    print("-" * 50)
    print("МЕНЮ")
    print("-" * 50)
    print("1 — Числа Улама без ограничений")
    print("2 — Числа Улама в интервале [a, b)")
    print("3 — Первые N чисел Улама (max_count)")
    print("4 — Показать все примеры")
    print("0 — Выход")
    print("-" * 50)

def _run_menu_item(choice):
    """Обрабатывает пункт меню. Возвращает False для выхода."""
    if choice == "0":
        print("Выход из программы. До свидания!")
        return False

    if choice == "1":
        try:
            n = int(input("Сколько чисел вывести? ").strip() or "10")
            print(ulam_sequence(max_count=n))
        except (TypeError, ValueError) as error:
            print(f"Ошибка: {error}")
    elif choice == "2":
        try:
            a = int(input("Введите a (>=1): ").strip() or "1")
            b_str = input("Введите b (Enter — без ограничения): ").strip()
            b = int(b_str) if b_str else None
            print(ulam_sequence(a=a, b=b))
        except (TypeError, ValueError) as error:
            print(f"Ошибка: {error}")
    elif choice == "3":
        try:
            n = int(input("Сколько чисел вывести? ").strip() or "5")
            print(ulam_sequence(max_count=n))
        except (TypeError, ValueError) as error:
            print(f"Ошибка: {error}")
    elif choice == "4":
        example_default_sequence()
        example_bounded_sequence()
        example_limited_count()
        example_type_error()
        example_value_error()
    else:
        print("Неизвестный пункт меню. Попробуйте снова.")

    print()
    return True

def main():
    """Точка входа: запускает меню в цикле."""
    print("Программа: Числа Улама")
    while True:
        _show_menu()
        choice = input("Выберите пункт меню: ").strip()
        if not _run_menu_item(choice):
            break

if __name__ == "__main__":
    main()

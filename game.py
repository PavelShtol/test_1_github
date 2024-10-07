def game_core_v3(number: int = 1) -> int:
    """
    Угадываем число с помощью бинарного поиска.

    :param number: Загаданное число (по умолчанию 1)
    :return: Количество попыток
    """
    # Инициализация диапазона поиска
    low, high = 1, 100
    # Инициализация счетчика попыток
    count = 0

    # Цикл бинарного поиска
    while low <= high:
        # Увеличиваем счетчик попыток
        count += 1
        # Вычисляем середину текущего диапазона
        mid = (low + high) // 2

        # Проверяем, угадали ли число
        if mid == number:
            # Возвращаем количество попыток, если число угадано
            return count
        # Если середина меньше загаданного числа, сдвигаем нижнюю границу
        elif mid < number:
            low = mid + 1
        # Если середина больше загаданного числа, сдвигаем верхнюю границу
        else:
            high = mid - 1

    # Возвращаем количество попыток в конце цикла
    return count

# Функция для оценки эффективности алгоритма
def score_game(game_core) -> int:
    """
    Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.

    :param game_core: Функция угадывания числа
    :return: Среднее количество попыток
    """
    import numpy as np
    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
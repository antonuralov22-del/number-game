def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
import random

def game_core_v3(number: int = 1) -> int:
    """
    Функция для угадывания числа методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2  # Методом бинарных алгоритмов берем середину диапазона

        if guess == number:
            return attempts  # Угаданное число
        elif guess < number:
            low = guess + 1  # Сужаем диапазон снизу
        else:
            high = guess - 1  # Сужаем диапазон сверху

    return attempts
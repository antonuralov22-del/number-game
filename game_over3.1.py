
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
        guess = (low + high) // 2  # Берем середину диапазона

        if guess == number:
            return attempts  # Число угадано!
        elif guess < number:
            low = guess + 1  # Сужаем диапазон снизу
        else:
            high = guess - 1  # Сужаем диапазон сверху

    return attempts

# Функция для проверки алгоритма
def score_game(game_core) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        game_core ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random.seed(1)  # Фиксируем RANDOM SEED для воспроизводимости
    random_array = [random.randint(1, 101) for _ in range(1000)]

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(sum(count_ls) / len(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

# Запуск проверки
if __name__ == "__main__":
    score_game(game_core_v3)


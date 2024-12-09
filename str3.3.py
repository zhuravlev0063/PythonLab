# Функция для вычисления квадратичного отклонения
def squared_deviation(a, b):
    return (a - b) ** 2

# Основная функция для обработки списка строк
def process_strings(strings):
    all_results = []

    for string in strings:
        # Найдем максимальный ASCII-код символа строки
        max_ascii = 0
        for char in string:
            ascii_value = ord(char)
            if ascii_value > max_ascii:
                max_ascii = ascii_value

        # Список для хранения квадратичных отклонений
        deviations = []
        char_pairs = []

        # Вычисляем отклонения между максимальным ASCII и разницей зеркальных символов
        for i in range(len(string) // 2):
            left_char = string[i]
            right_char = string[-(i + 1)]

            # Разница в ASCII кодах зеркальных символов
            left_ascii = ord(left_char)
            right_ascii = ord(right_char)
            diff = abs(left_ascii - right_ascii)

            # Квадратичное отклонение между max_ascii и разницей
            deviation = squared_deviation(max_ascii, diff)

            # Добавляем отклонение и соответствующие символы в список
            deviations.append(deviation)
            char_pairs.append((deviation, left_char, right_char))

        # Используем sorted для сортировки списка отклонений
        sorted_deviations = sorted(char_pairs)

        # Формируем отсортированную строку по отклонению
        sorted_string = ''.join(left for _, left, _ in sorted_deviations) + \
                        ''.join(right for _, _, right in sorted_deviations)

        # Сохраняем результат для текущей строки
        all_results.append((string, sorted_deviations, sorted_string))

    return all_results

# Пример использования
input_strings = [
    "строки с пример символами",
    "другаястрокадляанализа",
    "тестированиечастотсимволов"
]

results = process_strings(input_strings)

# Выводим результат
for input_string, sorted_deviations, sorted_string in results:
    print(f"Строка: '{input_string}'")
    print("Отклонения в порядке возрастания:", [deviation for deviation, _, _ in sorted_deviations])
    print("Отсортированная строка:", sorted_string)
    print("-" * 30)

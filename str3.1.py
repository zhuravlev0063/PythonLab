# Функция для подсчета частоты символов в строке
def count_frequencies(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


# Основная функция для вычисления разницы частот
def process_string(string, alphabet_frequencies):
    # Подсчет частот символов в строке
    freq_dict = count_frequencies(string)

    # Найдем самый часто встречаемый символ
    max_char = None
    max_freq = 0

    for char in freq_dict:
        freq = freq_dict[char] / len(string)  # вычисляем частоту символа
        if freq > max_freq:
            max_freq = freq
            max_char = char

    # Получим его частоту в языке (алфавите)
    if max_char in alphabet_frequencies:
        alphabet_freq = alphabet_frequencies[max_char]
    else:
        alphabet_freq = 0  # если символ отсутствует в списке стандартных частот

    # Рассчитываем разницу частот
    difference = abs(max_freq - alphabet_freq)

    return max_char, difference


# Пример стандартных частот для алфавита
alphabet_frequencies = {
    'а': 0.08,
    'б': 0.02,
    'в': 0.05,
    'г': 0.02,
    'д': 0.03,
    'е': 0.09,
    'ё': 0.01,
    'ж': 0.01,
    'з': 0.02,
    'и': 0.07,
    'й': 0.01,
    'к': 0.03,
    'л': 0.04,
    'м': 0.03,
    'н': 0.07,
    'о': 0.11,
    'п': 0.03,
    'р': 0.05,
    'с': 0.06,
    'т': 0.06,
    'у': 0.03,
    'ф': 0.01,
    'х': 0.01,
    'ц': 0.01,
    'ч': 0.01,
    'ш': 0.01,
    'щ': 0.01,
    'ъ': 0.01,
    'ы': 0.02,
    'ь': 0.02,
    'э': 0.01,
    'ю': 0.01,
    'я': 0.02
}


strings = [
    "примерстрокиссимволами",
    "другаястрокадляанализа",
    "тестированиечастотсимволов"
]

# Считаем разницу для каждой строки и собираем в список
differences = []
for string in strings:
    max_char, difference = process_string(string, alphabet_frequencies)
    differences.append((string, max_char, difference))

# Сортируем строки по величине разницы
differences.sort(key=lambda x: x[2])

# Вывод результатов
for string, max_char, difference in differences:
    print(f"Строка: {string}")
    print(f"Самый частый символ: {max_char}")
    print(f"Разница частот: {difference}")
    print("-" * 30)

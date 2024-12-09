# Функция для вычисления среднего значения ASCII-кодов тройки символов
def avg_ascii_weight(triplet):
    total = 0
    for char in triplet:
        total += ord(char)
    return total / len(triplet)

# Функция для нахождения всех троек символов в строке
def get_triplets(string):
    triplets = []
    for i in range(len(string) - 2):
        triplets.append(string[i:i+3])
    return triplets

# Функция для вычисления дисперсии
def variance(data):
    mean = sum(data) / len(data)
    total = 0
    for x in data:
        total += (x - mean) ** 2
    return total / len(data)

# Функция для вычисления квадратичного отклонения
def squared_deviation(a, b):
    return (a - b) ** 2

# Основная функция для обработки списка строк
def process_strings(strings):
    # Список для хранения результатов
    all_results = []

    # Определяем максимальный средний вес и дисперсию для первой строки
    first_string_triplets = get_triplets(strings[0])
    first_triplet_weights = [avg_ascii_weight(triplet) for triplet in first_string_triplets]
    first_variance = variance(first_triplet_weights)

    for string in strings:
        # Получаем все тройки символов
        triplets = get_triplets(string)

        # Вычисляем средние веса для каждой тройки символов
        triplet_weights = [avg_ascii_weight(triplet) for triplet in triplets]

        # Находим максимальный средний вес и дисперсию ASCII-кодов троек для данной строки
        max_weight = max(triplet_weights)
        string_variance = variance(triplet_weights)

        # Вычисляем квадратичное отклонение дисперсии от первой строки
        deviation = squared_deviation(string_variance, first_variance)

        # Сохраняем результат для текущей строки
        all_results.append((string, deviation, max_weight))

    # Сортируем строки по возрастанию квадратичного отклонения дисперсии
    all_results.sort(key=lambda x: x[1])

    return all_results

# Пример использования
input_strings = [
    "пример строкис с cимволами",
    "другаястрокадляанализа",
    "тестированиечастотсимволов"
]

results = process_strings(input_strings)

# Выводим результат
for input_string, deviation, max_weight in results:
    print(f"Строка: '{input_string}'")
    print(f"Квадратичное отклонение дисперсии: {deviation}")
    print(f"Максимальный средний вес ASCII: {max_weight}")
    print("-" * 30)

def sort_russian_flag(colors):
    # Определяем желаемый порядок цветов
    flag_order = ["белый", "синий", "красный"]

    # Используем сортировку на основе желаемого порядка
    sorted_colors = sorted(colors, key=lambda color: flag_order.index(color))

    return sorted_colors


# Пример массива
colors_array = ["белый", "синий", "красный", "белый", "красный", "синий"]

# Упорядочим массив
sorted_array = sort_russian_flag(colors_array)

# Выводим результат
print("Отсортированный массив:", sorted_array)

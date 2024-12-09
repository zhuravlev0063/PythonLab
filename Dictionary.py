def countries_and_cities():
    # Чтение количества стран
    n = int(input("Введите количество стран: "))

    # Инициализация словаря для хранения стран и городов
    country_city_dict = {}

    # Ввод данных для каждой страны
    for _ in range(n):
        # Разбиваем строку: первый элемент — страна, остальные — города
        data = input("Введите страну и города: ").split()
        country = data[0]
        cities = data[1:]
        # Добавляем страну как ключ и список городов как значение
        country_city_dict[country] = cities

    # Чтение количества городов, для которых нужно определить страну
    m = int(input("\nВведите количество городов для поиска: "))

    # Поиск страны для каждого введенного города
    for _ in range(m):
        city = input("Введите название города: ")
        # Поиск страны, в которой находится этот город
        for country, cities in country_city_dict.items():
            if city in cities:
                print(country)
                break


# Пример вызова функции
countries_and_cities()

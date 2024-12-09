def calculate_median_position(stations, total_fuel):
    # Сортировка станций по их расположению
    stations.sort()

    # Найдем середину по объему топлива
    half_fuel = total_fuel // 2

    cumulative_fuel = 0
    median_position = 0

    # Накапливаем количество топлива до тех пор, пока не достигнем середины
    for position, fuel in stations:
        cumulative_fuel += fuel
        if cumulative_fuel >= half_fuel:
            median_position = position
            break

    return median_position


def calculate_min_cost(N, K, V, stations):
    # Сумма необходимого топлива для всех станций
    total_fuel = sum(fuel for _, fuel in stations)

    # Найдем медианную позицию
    best_location = calculate_median_position(stations, total_fuel)

    # Рассчитаем минимальные затраты на доставку
    min_cost = 0
    for station, fuel_needed in stations:
        # Рассчитываем минимальное расстояние с учетом кольцевой дороги
        direct_dist = abs(best_location - station)
        circular_dist = K - direct_dist
        min_distance = min(direct_dist, circular_dist)

        # Количество рейсов
        trips = (fuel_needed + V - 1) // V  # округление вверх
        # Затраты = расстояние * количество рейсов
        min_cost += min_distance * trips

    return min_cost, best_location


# Пример использования:
def read_input(file_path):
    with open(file_path, 'r') as f:
        N, K, V = map(int, f.readline().split())
        stations = []
        for line in f:
            position, fuel = map(int, line.split())
            stations.append((position, fuel))
    return N, K, V, stations


file_a = 'file/27-123a.txt'
file_b = 'file/27-123b.txt'

N, K, V, stations = read_input(file_a)
min_cost, best_location = calculate_min_cost(N, K, V, stations)
print(f"Минимальные затраты: {min_cost}")
print(f"Расположение бензохранилища: {best_location} км")

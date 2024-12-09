# Найти элементы перед последним минимальным.
def find_before_last_min(arr):
    last_min_index = len(arr) - 1 - arr[::-1].index(min(arr))
    return arr[:last_min_index]

# Найти элементы после первого максимального.
def find_after_first_max(arr):
    first_max_index = arr.index(max(arr))
    return arr[first_max_index + 1:]

# Проверить, чередуются ли положительные и отрицательные числа.
def check_alternating_signs(arr):
    for i in range(1, len(arr)):
        if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0):
            return False
    return True

# Найти сумму элементов, которые попадают в интервал a..b.
def sum_in_interval(arr, a, b):
    return sum(x for x in arr if a <= x <= b)

# Найти количество элементов, которые больше суммы всех предыдущих.
def count_greater_than_previous_sum(arr):
    count = 0
    previous_sum = 0
    for num in arr:
        if num > previous_sum:
            count += 1
        previous_sum += num
    return count

# Меню
while True:
    print("\nВыберите задачу:")
    print("1. Найти элементы перед последним минимальным.")
    print("2. Найти элементы после первого максимального.")
    print("3. Проверить, чередуются ли положительные и отрицательные числа.")
    print("4. Найти сумму элементов, которые попадают в интервал a..b.")
    print("5. Найти количество элементов, которые больше суммы всех предыдущих.")
    print("0. Выйти.")

    choice = input("\nВведите номер задачи: ")

    if choice == "0":
        break

    arr = list(map(int, input("Введите целочисленный массив через пробел: ").split()))

    if choice == "1":
        print("Результат:", find_before_last_min(arr))
    elif choice == "2":
        print("Результат:", find_after_first_max(arr))
    elif choice == "3":
        print("Результат:", check_alternating_signs(arr))
    elif choice == "4":
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        print("Результат:", sum_in_interval(arr, a, b))
    elif choice == "5":
        print("Результат:", count_greater_than_previous_sum(arr))
    else:
        print("Некорректный выбор. Попробуйте снова.")

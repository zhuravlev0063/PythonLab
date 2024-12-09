# Функция для подсчета количества цифр числа, меньших 3
def count_digits_less_than_three(n):
    count = 0
    # Преобразуем число в строку для поочередного доступа к цифрам
    for digit in str(abs(n)):  # abs используется для работы с отрицательными числами
        if int(digit) < 3:
            count += 1
    return count

# Пример использования
n = int(input("Введите число: "))
result = count_digits_less_than_three(n)
print(f"Количество цифр числа {n}, меньших 3: {result}")

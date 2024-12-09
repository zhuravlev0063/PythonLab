import math


# Функция для проверки, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Функция для нахождения суммы непростых делителей
def sum_non_prime_divisors(n):
    divisors = []
    # Ищем делители числа n
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    # Отбираем непростые делители и находим их сумму
    non_prime_divisors_sum = sum(d for d in divisors if not is_prime(d))

    return non_prime_divisors_sum


# Пример использования
n = int(input("Введите число: "))
result = sum_non_prime_divisors(n)
print(f"Сумма непростых делителей числа {n}: {result}")

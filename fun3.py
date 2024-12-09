def is_prime(n): #Проверка, является ли число простым
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_digit_sum(n):#Вычисляет сумму простых цифр числа.
    return sum(int(digit) for digit in str(n) if is_prime(int(digit)))

def get_divisors(n):#Находит все делители числа.
    divisors = {i for i in range(1, n + 1) if n % i == 0}
    return divisors

def count_and_list_numbers(n): #перечисляет числа, которые не являются делителями, не совпадают с n и не совпадают с суммой простых цифр
    divisors = get_divisors(n)
    prime_sum = prime_digit_sum(n)

    valid_numbers = []
    for i in range(1, n + 1):
        if i not in divisors and gcd(n, i) != 1 and gcd(prime_sum, i) == 1:
            valid_numbers.append(i)

    return valid_numbers

def gcd(a, b): # Находит НОД
    while b:
        a, b = b, a % b
    return a

# Пример использования
number = int(input("Введите число: "))
result_numbers = count_and_list_numbers(number)
print(f"Количество чисел: {len(result_numbers)}")
print("Числа: ", result_numbers)

import random


def shuffle_words(sentence):
    # Разделим строку на слова
    words = sentence.split()

    # Перемешаем список слов
    random.shuffle(words)

    # Соединим слова обратно в строку
    shuffled_sentence = ' '.join(words)
    return shuffled_sentence


# Пример использования
input_sentence = input("Введите строку: ")
output_sentence = shuffle_words(input_sentence)
print("Перемешанная строка:", output_sentence)

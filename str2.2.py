def count_even_length_words(sentence):
    # Разделим строку на слова
    words = sentence.split()

    # Подсчитаем количество слов с четным числом символов
    even_length_count = sum(1 for word in words if len(word) % 2 == 0)

    return even_length_count


# Пример использования
input_sentence = input("Введите строку: ")
even_length_words_count = count_even_length_words(input_sentence)
print("Количество слов с четным количеством символов:", even_length_words_count)

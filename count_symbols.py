import string

def count_word_occurrences(text):
    # Удаляем знаки припенания из текста
    text = text.translate(str.maketrans("", "", string.punctuation))
    print(text)

    # Разбиваем текст на слова и приводим к нижнему регистру
    words = text.lower().split()

    # Создаём словарь для подчёта вхождений слов
    word_count = {}

    # Считаем вхождения каждого слова
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Пример использования
text = "Python is an amazing language.Python programming is fun!"
result = count_word_occurrences(text)
print(result)


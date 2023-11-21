"""
Дуже поширена помилка помилка - це повторення слів.
Так, у попередньому реченні така помилка була допущена.
Необхідно виправити кожне таке повторення слів. Контрольний текст:
"Дуже поширена помилка помилка - це лише повторення повторення слова слова.
Смішно, чи чи не так? Це - книга книгарні."
"""

words = "Дуже поширена помилка помилка - це лише повторення повторення слова слова . " \
        "Смішно, чи чи не так? Це - книга книгарні.".split()

w2 = list()
w2.append(words[0])
for i in range(1, len(words)):
    if words[i - 1] != words[i]:
        w2.append(words[i])
clean_words = " ".join(w2)
print(clean_words)






"""
uniquewords = dict((word,words.count(word)) for word in set(words))
print(uniquewords)
"""
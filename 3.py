"""
Розробити скрипт, який буде отримувати текст і виводити у консоль всі e-mail,
які знаходяться в тексті. Для визначення e-mail, слід використати стандарт RFC 5322.
"""

import re
import math

text = 'bub ubuc herryla abuba@gmail.com  @ala'
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def mailAsShifr(m):
    return [pow(ord(c), 3) for c in list(m)]

def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email", "--", email, mailAsShifr(email))
    else:
        print("Invalid email")

for i in text.split():
    isValid(i)








# print(text)
# print(list(text))
# print([math.pow(ord(i), 3) for i in list(text)])





"""
text = 'bub ubuc herryla abuba@gmail.com  @ala'
words = text.split()
for w in words:
    if w.find('@') > 0:
        print(w)
"""

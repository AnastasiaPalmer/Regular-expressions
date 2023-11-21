import re

"""
Великі числа зручно читати, якщо їхні цифри розділені комами на трійки.
Розробіть скрипт, який отримує текст і в кожному числі, яке є в тексті, додає коми де потрібно.
"""


def my_value(number):
    return "{:,}".format(number)


# print(my_value(100000000000))
# print(my_value('kuku 50000 nu'))
text = 'now there are more than 50000 died orks after 180 days ( 4320 hours ) of war'
cre = re.compile('^\\d+$')
newt = []
for w in text.split():
    if cre.match(w):
        newt.append(my_value(int(w)))
    else:
        newt.append(w)
print(" ".join(newt))
"""














n1 = 4567082
n2 = 560867956
n3 = "nu ka 120000"


def add_char(n, char):
    sn = str(n)
    rn = sn[::-1]
    return char.join(rn[s:s+3] for s in range(0, len(sn), 3))[::-1]

print(add_char(n1, ','))
print(add_char(n2, ','))
print(add_char(n3, ','))

text = "1234567."
print(text)
print(text[::-1])
"""

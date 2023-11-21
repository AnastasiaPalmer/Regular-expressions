
"""
Розробіть скрипт, який буде брати перші літери кожного слова
та створювати з нього абревіатуру (н-д, НАСА, ЗВО і т.д.).
Чим абревіатура відрізняється від акроніму та акровірша?
"""

def acronym(stng):
    oupt = stng[0]

    for i in range(1, len(stng)):
        if stng[i - 1] == ' ':
            oupt += stng[i]

    oupt = oupt.upper()
    return oupt


inpt1 = "Akuna matata"
inpt2 = "Computer Science Engineering"
inpt3 = "High Integrity Mobility Artillery Rocket System"

print([acronym(phrase) for phrase in (inpt1, inpt2, inpt3)])







"""
text = input("Enter text: ")
line = text.split()
if len(line) > 1:
    line = line[0:1]
    print(line)
"""


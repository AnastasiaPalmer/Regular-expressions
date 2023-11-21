
"""
Розробіть скрипт, який буде порівнювати пароль,
що вводить користувач з шаблоном, зашитим у коді.
При цьому порівняння не повинно враховувати регістр,
пробіли та всі інші розділові знаки, крім дефісу.
"""

import re
sec = re.compile('buba[0-9][0-9]$', re.IGNORECASE)

while True:
    w = input('type a pasw:')

    if w =='q' or w == '':
        break

    if sec.match(w):
        print('Ok, matched!!!', w)
    else:
        print('Get out, balbes! Try again...')

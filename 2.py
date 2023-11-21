"""
Розробити скрипт, який буде отримувати номер авто та
визначати валідність номеру та регіон реєстрації.
Номера, що можуть бути введені відповідають поточному
українському законодавству (лише стандартні номери,
номери на замовлення не використовуємо).
Використайте лише 3 регіони реєстрації України.
"""


def getRegion2(code):
    regions = {'AA': 'Kiev', 'AX': 'Kharkiv', 'AH': 'Donetsk'}      # словник

    code = str(code).upper()                                        # захист від манюнь

    if len(code) > 2:
        code = code[0:2]                                            # кромсалка

    if code in regions.keys():
        ans = regions[code]
    else:
        ans = 'Ukraine'
    print("region {} => {}".format(code, ans))


reg = input('Licence plate: ')
getRegion2(reg)

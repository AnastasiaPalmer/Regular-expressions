def fun(phrase):
    res = 0
    for lett in phrase:
        res += (lett.lower() in 'аоуиіеяюєї')
    return res


hik1 = "Ще не померла! / Закінчується осінь, / Я йду за обрій."                # Haiku
hik2 = "Ночую просто неба. / Виє пес. / Теж допекла, мабуть, осіння мряка!"    # Not a haiku
hik3 = "Вода замерзла, / Розколовши глечик. / І тріск раптовий розбудив мене"  # Not a haiku


print(['Не хайку!', 'Хайку!'][[5, 7, 5] == [fun(phrase) for phrase in hik1.split("/")]])
print([fun(phrase) for phrase in hik1.split("/")])
print(['Не хайку!', 'Хайку!'][[5, 7, 5] == [fun(phrase) for phrase in hik2.split("/")]])
print([fun(phrase) for phrase in hik2.split("/")])
print(['Не хайку!', 'Хайку!'][[5, 7, 5] == [fun(phrase) for phrase in hik3.split("/")]])
print([fun(phrase) for phrase in hik3.split("/")])


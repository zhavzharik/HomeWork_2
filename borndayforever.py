year = 0
day = 0
while year != 1799:
    year = int(input('В каком году родился А.С. Пушкин? '))
    if year == 1799:
        print('Верно!')
    else:
        print('Неверный год рождения!')
while day != '6 июня':
    day = input('А в какой день родился А.С. Пушкин? ')
    if day == '6 июня':
        print('Верно!')
    elif day == 'шестого июня':
        print('Верно!')
        break
    elif day == '06.06':
        print('Верно!')
        break
    elif day == '6.06':
        print('Верно!')
        break
    else:
        print('Неверный день рождения!')

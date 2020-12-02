# Будем спрашивать год рождения:
# М.В. Ломоносов - 1711
# Фидель Кастро - 1926
# Л.Н. Толстой - 1828
# Д.И. Менделеев - 1834
# И.В. Грозный - 1530

print('Викторина "Год рождения знаменитых людей" ')
answer = 0
while answer != 'нет':
    true_answer = 0
    false_answer = 0
    year = int(input('В каком году родился М.В. Ломоносов? '))
    if year == 1711:
        true_answer +=1
    else:
        false_answer +=1
    year = int(input('В каком году родился Фидель Кастро? '))
    if year == 1926:
        true_answer += 1
    else:
        false_answer += 1
    year = int(input('В каком году родился Л.Н. Толстой? '))
    if year == 1828:
        true_answer += 1
    else:
        false_answer += 1
    year = int(input('В каком году родился Д.И. Менделеев? '))
    if year == 1834:
        true_answer += 1
    else:
        false_answer += 1
    year = int(input('В каком году родился И.В. Грозный? '))
    if year == 1530:
        true_answer += 1
    else:
        false_answer += 1
    print('Количество правильных ответов: ', true_answer)
    print('Количество неправильных ответов: ', false_answer)
    print('% правильных ответов: ', round(true_answer*100/(true_answer + false_answer), 2), '%')
    print('% неправильных ответов: ', round(false_answer*100/(true_answer + false_answer), 2), '%')
    print('')
    answer = input('Хочешь сыграть еще раз? Напиши, да или нет? ')
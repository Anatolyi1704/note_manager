username = input ("Введите ваше имя: ")
title = input ("Введите заголовок заметки: ")
title1 = input ("Введите заголовок первой части: ")
title2 = input ("Введите заголовок второй части: ")
title3 = input ("Введите заголовок третьей части: ")
titles = [title1, title2, title3]
content = input("Введите содержание заметки: ")
status = input ("Введите статус заметки: ")
created_date = input ("Введите дату создания (в формате ДД.ММ.ГГГГ): ")
issue_date = input ("Введите дату окончания (в формате ДД.ММ.ГГГГ): ")
note = {
    "Имя пользователя:" : username,
    "Заголовок:" : title,
    "Подзаголовки:": titles,
    "Содержание:" : content,
    "Статус:" : status,
    "Дата создания:" : created_date[0:5],
    "Дата окончания:" : issue_date[0:5],
}
print(note)
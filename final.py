username = input ("Введите ваше имя: ")
title = input ("Введите заголовок заметки: ")
title1 = input ("Введите заголовок первой части: ")
title2 = input ("Введите заголовок второй части: ")
title3 = input ("Введите заголовок третьей части: ")
title_0 = [title1, title2, title3]
content = input("Введите содержание заметки: ")
status = input ("Введите статус заметки: ")
created_date = input ("Введите дату создания (в формате ДД.ММ.ГГГГ): ")
issue_date = input ("Введите дату окончания (в формате ДД.ММ.ГГГГ): ")
note = [username, title, content, status, created_date[0:5], issue_date[0:5], title_0]
print(note)
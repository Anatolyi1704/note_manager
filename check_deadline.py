from datetime import timedelta

notes=[]
note={}
import datetime
while True:
    username = input ("Введите ваше имя: ")
    if username.lower() == 'stop' or username.lower() == '':
        break
    else:    
        #title = input ("Введите заголовок (или оставьте пустым для завершения): ")
        while True:
            title = input ("Введите заголовок (или оставьте пустым для завершения): ")
            #title = input ("Введите заголовок (или оставьте пустым для завершения): ") :
            if title.lower() == 'stop' or title.lower() == '':
                break
            else: 
                content = input('Введите содержание заметки: ')
                while True:
                    status = input ("Выберите статус заметки (введите цифру): 1.Выполнено, 2.В процессе, 3.Отложено: ")
                    if status == "1":
                        status = "Выполнено"
                        break
                    elif status == "2":
                        status = "В процессе"
                        break
                    elif status == "3":
                        status = "Отложено"
                        break
                    else:
                        print("Ошибка, введите цифру заново")
                    continue
                print("Статус заметки:", status)
                current_date = datetime.datetime.now().strftime('%d-%m-%Y')
                print("Сегодня", current_date)
                created_date = input ("Введите дату создания (в формате ДД.ММ.ГГГГ): ")
                issue_date = datetime.datetime.strptime(input ("Введите дату окончания (в формате ДД.ММ.ГГГГ): " ))
                if current_date > issue_date:
                    difference = datetime.timedelta(current_date - issue_date)
                    print(f'Внимание! Дедлайн истёк {difference} дня назад')
                elif current_date == issue_date:
                    print("Внимание! Дедлайн истекает сегодня!")
                elif current_date < issue_date:
                    difference = issue_date - current_date
                    print(f'До дедлайна осталось {difference} дня')
                note = {
                "Имя пользователя" : username,
                "Заголовок" : title,
                "Содержание" : content,
                "Статус" : status,
                "Дата создания" : created_date[0:5],
                "Дата окончания" : issue_date[0:5],
            }
            notes.append(note)
for note in notes:
    print(note)
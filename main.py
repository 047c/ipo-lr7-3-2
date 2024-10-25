import json  # Подключаем json

linii = '-' * 22  # Добавляем элемент дизайна
with open("dump.json", 'r', encoding='utf-8') as file:  # Открываем файл, выдав имя файл
    dump = json.load(file)  # Загружаем в перменную дамп содержимое json
while True:  # Пока истинно(программа выполняется, пока не будет завершена извне)
    status = False
    find = input("Введите номер квалификации: ")  # Просим ввести номер квалификации
    for item in dump:  # Для  каждого предмета
        if item['model'] == 'data.skill':  # Если имеет значение квалификации в поле модель
            if item["fields"]['code'] == find:  # Если код равен
                for specialty in dump:
                    if specialty['model'] == 'data.specialty':
                        if specialty['pk'] == item['fields']['specialty']:
                            print(f'{linii} Найдено {linii}')
                            print(
                                f'{specialty["fields"]["code"]} >> Специальность'
                                f' {specialty["fields"]["title"]}, {specialty["fields"]["c_type"]}')
                            print(f"{item['fields']['code']} >> Квалификация {item['fields']['title']}")
                            print(linii + linii)
                            status = True
    if not status:
        print(f'{linii} Не найдено {linii}')
        print("Не получилось ничего найти по вашей квалификации")
        print(linii + linii)
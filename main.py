import json
# Открываем файл Json для чтения. 'имя джейсона''чтение'
with open('package.json', 'r') as json_file:
    # Назначаем джейсон в дату
    data = json.load(json_file)

while True:
    name = input("Enter name")
    surname = input("Enter surname")
    # Создаем новую структуру данных для добавления
    new_person = {
        "name": name,
        "surname": surname
    }

    # Используем метод списка для добавления новых элементов
    data["Users"].append(new_person)
    # Опять открываем файл джейсона но уже для записи
    with open('package.json', "w") as json_file:
        # Пишем команду (переменная в которой джейсон, переменная обработчик, кол-во табуляций)
        json.dump(data, json_file, indent=2)


#  Записываем в переменную дата json
# data = json.loads('')
#
# for item in data['response']['items']:
#     del item['id']
#     item['likes'] = "booo"
#
# print(data['response']['items'])
#
# with open('package.json', 'w') as file:
#     json.dump(data, file, indent=2)


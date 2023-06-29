# import json
#
# with open("example.json", "r") as json_file:
#     a = json.load(json_file)
#     print(a)
# # Функция для удаления элемента словаря
#
# del a["Media"]["OnlyFans"]
#
# a["Mass"] = [1, "h", {"a":1}, [1,2,3]]
#
# # Вывод информации из файла json
# print(json.dumps(a, indent=2))
#
# with open("example.json", "w") as json_file:
#     json.dump(a, json_file, indent=4)

import json

# Открываем Json файл
with open("package.json", "r") as json_file:
    file = json.load(json_file) # Записываем файл в переменную, чтобы через неё работать

# Обращаемся к ключю Нейм и меняем ему значение
file["Name"] = "Alex"

# Производим запись изменений в json файл
with open("package.json", "w") as json_file:
    json.dump(file, json_file, indent=1)
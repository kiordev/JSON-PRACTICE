import json

with open("package.json", 'r') as json_file:
    data = json.load(json_file)

# Вывод количества фильмов
print(f"Количество фильмов: {len(data['Films'])}")


# Список всех жанров
genres = set()
for item in data['Films']:
    genres.add(item['genre'])
print(genres)


# user_year = int(input("Введите год: "))
# for item in data['Films']:
#     if user_year == item['year']:
#         print(item['title'], item['year'])

# Пользователь вводит год выпуска
user_min_year = int(input("Введите начальный год: "))
user_max_year = int(input("Введите последний год: "))
for item in data['Films']:
    if item['year'] >= user_min_year and item['year'] <= user_max_year:
        print(item['title'], item['year'])






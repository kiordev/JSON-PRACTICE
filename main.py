import json as js

data = {
    "to_user": "Sergey",
    "text": "hello",
    "attachments": ['1.png', '2.wav'],
    "type": 'direct',
    'demolition': None,
}

json_str = js.dumps({1, 2, 3}) #py obj to json string

print(json_str)
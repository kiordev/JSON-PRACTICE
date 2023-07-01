string_json = '{"k_int: 100, "k_bool":false}'
dict_example = {"k_int": 100, "k_bool": False}

import json

with open("package.json", "r") as f:
    dict_data = json.loads(f)


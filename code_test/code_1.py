import json

dict_1 = {"a": 1}
dict_1.update({"b": 2})
dict_1["c"] = 3
print(dict_1)
print(json.dumps(dict_1, indent=2))

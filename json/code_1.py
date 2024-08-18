import json

print("# Convert Python object to JSON")
dict_1 = {"name": "John", "age": 25}
print(dict_1)
print(type(dict_1))
json_str = json.dumps({"name": "John", "age": 25})
print(type(json_str))
print(json_str)

print("# Convert JSON to Python object")
data_str = '{"name": "John", "age": 25}'
print(data_str)
print(type(data_str))
python_dict = json.loads(data_str)
print(python_dict)
print(type(python_dict))

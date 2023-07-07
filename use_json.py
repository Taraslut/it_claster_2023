import json

obj = json.load(open("sample.json"))

print(obj)
print(type(obj))

print(obj['notes'][3]["Location"])
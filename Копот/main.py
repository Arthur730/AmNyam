import json

file_path = 'data/data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

print(data)
import json


def loader(path):
    with open(path) as file:
        data = json.load(file)
        return data
        # print(data)

# loader('gendiff/input_data/file2.json')

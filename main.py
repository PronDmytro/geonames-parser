import json


def is_exist(code):
    for codeLine in data:
        if codeLine["postalCode"] == code:
            return True
    return False


file1 = open("data/file.txt", "r", encoding='utf-8')

Lines = file1.readlines()

data = []

for line in Lines:
    blocks = line.split('\t')
    if not is_exist(blocks[1]):
        line_data = {"postalCode": blocks[1], "ort": blocks[2], "lat": float(blocks[9]), "lon": float(blocks[10])}
        data.append(line_data)

with open('output/file.json', 'w') as fout:
    json.dump(data, fout)

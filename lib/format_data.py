import json
import os


def format_data():
    file_list = [i for i in os.listdir('data') if i.endswith('.json') and i != 'UnofficialUnicode.json']
    all_data = {}
    for file_name in file_list:
        with open(f'data/{file_name}', 'r', encoding='utf-8')as f:
            all_data.update(json.load(f))
    with open('data/UnofficialUnicode.json', 'w')as f:
        f.write(json.dumps(all_data,indent=4))


if __name__ == '__main__':
    format_data()

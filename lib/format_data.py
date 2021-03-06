import json
import os


def format_data():
    file_list = [i for i in os.listdir('data') if i.endswith('.json')]
    all_data = {}
    for file_name in file_list:
        with open(f'data/{file_name}', 'r', encoding='utf-8')as f:
            all_data.update(json.load(f))
    all_data = {r"\u" + k.lower(): r"\u" + v.lower() for k, v in all_data.items()}

    with open('data/unofficial_unicode.py', 'w')as f:
        f.write('import json\n')
        f.write('''
def format_string_remove_unofficial_char(text):
    result = ''
    before_is_unofficial = False
    before_unicode = None
    for char in text:
        # Gets the unicode of the character
        char_unicode = char.encode('unicode_escape').decode().lower()
        if before_is_unofficial and char_unicode == before_unicode:
            continue
        # If this character is an unofficial character, then get the correct unicode
        if char_unicode in UNOFFICIALUNICODE.keys():
            char_unicode = UNOFFICIALUNICODE[char_unicode]
            if char_unicode == before_unicode:
                continue
            char = char_unicode.encode('latin-1').decode('unicode_escape')
            before_is_unofficial = True
        else:
            before_is_unofficial = False
        result += char
        before_unicode = char_unicode
    return result\n
''')

        f.write('UNOFFICIALUNICODE = '+json.dumps(all_data, indent=4))


if __name__ == '__main__':
    format_data()

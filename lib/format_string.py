from data.unofficial_unicode import UNOFFICIALUNICODE


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
    return result


if __name__ == '__main__':
    format_string('⽹网 武汉⻓长江全媒体有限公司')

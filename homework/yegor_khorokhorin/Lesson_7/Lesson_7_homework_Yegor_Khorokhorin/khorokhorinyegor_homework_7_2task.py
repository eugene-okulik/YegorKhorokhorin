words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def keys(words_dict):
    for key, value in words_dict.items():
        print(key * value)


keys(words)

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
new_text = []
for word in words:
    punctuation = ".,"
    words_without_punctuation = word.rstrip(punctuation)
    suffix = word[len(words_without_punctuation):]
    new_text.append(words_without_punctuation + "ing" + suffix)
print(' '.join(new_text))

text = input()
words = text.split()
for word in words:
    lw_word = str.lower(word)
    if lw_word.startswith(("https://", "http://", "www.")):
        print(word)

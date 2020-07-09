word = input()

word = word.lower()

if "_" in word:
    output = [w.capitalize() for w in word.split("_")]
    print("".join(output))
else:
    print(word.capitalize())

digits = input()

print([int(x) for x in list(digits) if int(x) % 2 == 1])

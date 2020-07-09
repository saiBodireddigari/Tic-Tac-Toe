sent = input().split(" ")

output = [word for word in sent if word.endswith("s")]

print("_".join(output))

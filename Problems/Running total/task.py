digits = input()
count = 0
fib_seq = []

for x in digits:
    fib = count + int(x)
    count = fib
    fib_seq.append(fib)

print(fib_seq)

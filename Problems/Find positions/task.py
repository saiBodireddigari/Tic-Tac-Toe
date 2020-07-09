# put your python code here
seq_num = input().split()

number = int(input())

indexes = [str(i) for i, val in enumerate(seq_num) if val == str(number)]

print(" ".join(indexes) or "not found")

n = input()
n_list = [int(x) for x in n]

avg_list = [((n_list[a] + n_list[a + 1]) / 2) for a in range(len(n_list) - 1)]

print(avg_list)

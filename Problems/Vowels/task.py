vowels = 'aeiou'
# create your list here

word = input()
print([x for x in list(word) if x in vowels])

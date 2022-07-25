string = "python is an interpreted and dynamic programming language"
print(string)
string_list = string.split(" ")
char_list = []
dictionary = {}
for word in string_list:
    char_list.append(word[0])

char_list = list(set(char_list))

print(char_list)

for c in char_list:
    dictionary[c] = []
    for word in string_list:
        if c == word[0]:
            dictionary[c].append(word)

print(dictionary)
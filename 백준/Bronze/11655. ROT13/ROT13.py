sentence = input()

char = list(sentence)

for i in range(len(char)):
    if 'A' <= char[i] <= 'Z': 
        char[i] = chr((ord(char[i]) - ord('A') + 13) % 26 + ord('A'))
    elif 'a' <= char[i] <= 'z': 
        char[i] = chr((ord(char[i]) - ord('a') + 13) % 26 + ord('a'))

print(''.join(char))

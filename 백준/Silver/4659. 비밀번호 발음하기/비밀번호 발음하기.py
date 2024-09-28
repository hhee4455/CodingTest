def password(word):
    word_set = set(word)
    word_array = list(word)
    mo = set("aeiou")
    
    if not any(char in mo for char in word_set):
        return False

    a_count = 0
    b_count = 0
    for i in range(len(word_array)):
        if word_array[i] in mo:
            a_count += 1
            b_count = 0
        else:
            b_count += 1
            a_count = 0
        if a_count == 3 or b_count == 3:
            return False

    for i in range(1, len(word_array)):
        if word_array[i] == word_array[i-1]:
            if word_array[i] not in {'e', 'o'}:
                return False
    
    return True

while True:
    word = input()
    if word == "end":
        break
    
    if password(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")

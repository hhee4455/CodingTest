n = int(input())
num_array = []

for _ in range(n):
    word = input()
    current_number = ""
    
    for char in word:
        if char.isdigit(): 
            current_number += char
        else:
            if current_number:
                num_array.append(int(current_number)) 
                current_number = ""
    
    if current_number:
        num_array.append(int(current_number))

num_array.sort()

for result in num_array:
    print(result)

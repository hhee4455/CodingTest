n = int(input())

room = [input() for _ in range(n)]

horizontal_count = 0
vertical_count = 0

for i in range(n):
    count = 0
    for j in range(n):
        if room[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                horizontal_count += 1
            count = 0
    if count >= 2:  
        horizontal_count += 1

for j in range(n):
    count = 0
    for i in range(n):
        if room[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                vertical_count += 1
            count = 0
    if count >= 2: 
        vertical_count += 1

print(horizontal_count, vertical_count)

h, w = map(int,input().split())
result = []

for i in range(h):
    map_array = list(input())
    count = [-1 for _ in range(w)]
    for j in range(w):
        if map_array[j] == 'c':
            count[j] = 0

    for j in range(1,w):
        if count[j-1] == 0 and count[j] != 0:
            count[j] = 1
        elif count[j] != 0 and count[j-1] != -1:
            count[j] = count[j-1] + 1
            
    result.append(count)

for i in range(h):
    print(*result[i])


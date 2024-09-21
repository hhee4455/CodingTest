k = int(input())
farm = []

for i in range(6):
    m, n = map(int, input().split())
    farm.append((m, n))

max_x = 0
max_y = 0
for direction, length in farm:
    if direction == 1 or direction == 2: 
        if length > max_x:
            max_x = length
    elif direction == 3 or direction == 4: 
        if length > max_y:
            max_y = length

max_x_index = [i for i in range(6) if farm[i][1] == max_x][0]
max_y_index = [i for i in range(6) if farm[i][1] == max_y][0]

small_x = abs(farm[(max_x_index - 1) % 6][1] - farm[(max_x_index + 1) % 6][1])
small_y = abs(farm[(max_y_index - 1) % 6][1] - farm[(max_y_index + 1) % 6][1])

area_a = max_x * max_y
area_b = small_x * small_y

area = area_a - area_b
print(area * k)

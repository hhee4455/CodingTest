n = int(input())
array = []

for i in range(n):
    x,y = map(int,input().split())
    array_a = [x,y]
    array.append(array_a)

sort_array = sorted(array, key= lambda x : (x[0],x[1]))

for i in range(n):
    print(*sort_array[i])


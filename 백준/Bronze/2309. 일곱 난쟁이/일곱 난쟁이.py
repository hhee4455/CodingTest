from itertools import combinations

array = []

for i in range(9):
    tall = int(input())
    array.append(tall)

for j in combinations(array, 7):
    sum_a = sum(j)
    sorted_j = sorted(j)
    if sum_a == 100:
        for k in sorted_j:
            print(k)
        break

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
best_sum = 0

for comb in combinations(cards, 3):
    current_sum = sum(comb)
    if current_sum <= m and current_sum > best_sum:
        best_sum = current_sum

print(best_sum)
def knapsack(i, w, items, memo):
    if i < 0: 
        return 0

    if memo[i][w] != -1: 
        return memo[i][w]

    weight, value = items[i]

    if weight > w:
        memo[i][w] = knapsack(i - 1, w, items, memo)  # 물건을 넣을 수 없는 경우
    else:
        memo[i][w] = max(knapsack(i - 1, w, items, memo),
                         knapsack(i - 1, w - weight, items, memo) + value)

    return memo[i][w]

n, k = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(n)]
memo = [[-1] * (k + 1) for _ in range(n)]
print(knapsack(n - 1, k, items, memo))
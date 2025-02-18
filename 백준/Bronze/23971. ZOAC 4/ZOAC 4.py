def solution(h, w, n, m):
    x = h - 1
    x_a = n + 1
    x_result = 1 + (x // x_a)

    y = w - 1
    y_a = m + 1
    y_result = 1 + (y // y_a)

    return x_result * y_result

h, w, n, m = map(int, input().split())
print(solution(h, w, n, m))

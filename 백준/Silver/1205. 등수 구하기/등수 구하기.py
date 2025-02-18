def solution(n, s, p, scores):
    if n == 0:
        return 1

    rank = 1
    for i in range(n):
        if s > scores[i]:
            break
        if s < scores[i]:
            rank += 1

    if n == p and s <= scores[-1]:
        return -1

    return rank
    
n, s, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

print(solution(n, s, p, scores))

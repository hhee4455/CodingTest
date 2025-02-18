N = int(input())
M = int(input())
pos = list(map(int, input().split()))

left = 1
right = N
answer = N
while left <= right:
    mid = (left+right) // 2
    l = mid
    covered = 0
    for p in pos:
        if p - l > covered:
            break
        covered = p + l

    if covered >= N:
        if answer > l:
            answer = l
        right = mid - 1
    else:
        left = mid + 1

print(answer)
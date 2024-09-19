n, m = map(int,input().split())
j = int(input())

apple = list(int(input()) for _ in range(j))

count = 0
left = 1

for apple_drop in apple:

    right = left + m - 1

    if left > apple_drop:
        count += left - apple_drop
        left = apple_drop

    elif right < apple_drop:
        count += apple_drop - right
        left += apple_drop - right

print(count)

T = int(input())
for test_case in range(1, T + 1):
    numbers = map(int, input().split())
    total = 0

    for num in numbers:
        if num % 2 == 0:
            total += num

    print(f"#{test_case}:{total}")

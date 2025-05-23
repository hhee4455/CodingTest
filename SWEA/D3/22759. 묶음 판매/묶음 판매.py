T = int(input())
for test_case in range(1, T + 1):
    L, R = map(int, input().split())

    # For all N between L and R to have remainders >= X/2 when divided by X:
    # 1. R-L+1 <= X/2 (to avoid a complete cycle of remainders)
    # 2. The starting remainder (L mod X) should be >= X/2

    # From condition 1, X >= 2*(R-L+1)
    min_X = 2 * (R - L + 1)

    # From condition 2, we need to find an X such that L mod X >= X/2
    # This is possible if there exists an X such that L mod X >= X/2 and X >= min_X

    # For X = 2*L, L mod X = L, and L >= X/2 = L, which is always true
    # So, if min_X <= 2*L, we can choose X = 2*L and both conditions are satisfied

    if min_X <= 2 * L:
        print("yes")
    else:
        print("no")
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = [''] * (N + 1)
    picked = set()
    
    A_index = 0
    B_index = 0
    turn = 0

    while len(picked) < N:
        if turn == 0:
            while A_index < N and A[A_index] in picked:
                A_index += 1
            if A_index < N:
                p = A[A_index]
                result[p] = 'A'
                picked.add(p)
                A_index += 1
        else:
            while B_index < N and B[B_index] in picked:
                B_index += 1
            if B_index < N:
                p = B[B_index]
                result[p] = 'B'
                picked.add(p)
                B_index += 1

        turn ^= 1

    print(''.join(result[1:]))  
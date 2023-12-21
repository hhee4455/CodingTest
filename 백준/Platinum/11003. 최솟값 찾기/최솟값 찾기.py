from collections import deque

def find_minimum_values(N, L, A):
    result = []
    deque_min_indices = deque()

    for i in range(N):
        while deque_min_indices and deque_min_indices[0] < i - L + 1:
            deque_min_indices.popleft()

        while deque_min_indices and A[deque_min_indices[-1]] > A[i]:
            deque_min_indices.pop()

        deque_min_indices.append(i)

        result.append(A[deque_min_indices[0]])

    return result


N, L = map(int, input().split())
A = list(map(int, input().split()))

result = find_minimum_values(N, L, A)
print(" ".join(map(str, result)))
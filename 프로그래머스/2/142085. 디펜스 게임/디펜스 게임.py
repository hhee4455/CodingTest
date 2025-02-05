import heapq

def solution(n, k, enemy):
    max_heap = []

    for i in range(len(enemy)):
        heapq.heappush(max_heap, -enemy[i])
        n -= enemy[i]  

        if n < 0:
            if k > 0:
                n += -heapq.heappop(max_heap)
                k -= 1
            else:
                return i  

    return len(enemy)

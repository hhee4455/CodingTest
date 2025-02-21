import sys
import heapq

input = sys.stdin.readline

n = int(input())
min_heap = []

for i in range(n):
    row = list(map(int,input().split()))
    for num in row:
        if len(min_heap) < n:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)
            
print(min_heap[0])
import heapq

def solution(k, score):
    result = []
    heap = []
    
    for i in range(len(score)):
        heapq.heappush(heap, score[i])
        
        if len(heap) > k:
            heapq.heappop(heap)
        
        result.append(heap[0])
        
    return result
            
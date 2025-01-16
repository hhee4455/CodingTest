def solution(sequence, k):
    result = []
    start, end = 0, 0
    current_sum = 0  

    while end < len(sequence):
        current_sum += sequence[end]

        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1

        if current_sum == k:
            result.append((start, end))

        end += 1 
    
    result.sort(key=lambda x: x[1] - x[0])
    return list(result[0])

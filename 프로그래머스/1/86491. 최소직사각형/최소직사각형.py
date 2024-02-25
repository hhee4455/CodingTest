def solution(sizes):
    max_a = []
    max_b = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        max_a.append(sizes[i][0])
        max_b.append(sizes[i][1])
    max_a.sort(reverse = True)
    max_b.sort(reverse = True)
    
    return max_a[0] * max_b[0]
def solution(m, n, startX, startY, balls):
    result = []
    
    for a, b in balls:
        candidates = [
            ((-a, b), (startX - (-a)) ** 2 + (startY - b) ** 2), 
            ((2 * m - a, b), (startX - (2 * m - a)) ** 2 + (startY - b) ** 2),
            ((a, -b), (startX - a) ** 2 + (startY - (-b)) ** 2),
            ((a, 2 * n - b), (startX - a) ** 2 + (startY - (2 * n - b)) ** 2)  
        ]
        

        min_dist = float('inf')
        for (x, y), dist in candidates:
            if (x == startX and min(startY, y) < b < max(startY, y)) or \
               (y == startY and min(startX, x) < a < max(startX, x)):
                continue
            min_dist = min(min_dist, dist)
        
        result.append(min_dist)
    
    return result

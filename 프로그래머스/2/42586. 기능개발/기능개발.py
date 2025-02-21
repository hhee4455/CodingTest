import math
from collections import deque

def solution(progresses, speeds):
    days = deque([math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)])
    result = []

    while days:
        count = 1
        first = days.popleft()  

        while days and first >= days[0]:  
            days.popleft()
            count += 1

        result.append(count) 

    return result

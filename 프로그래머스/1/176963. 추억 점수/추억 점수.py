from collections import deque

def solution(name, yearning, photo):
    result = []
    score_map = {na: year for na, year in zip(name, yearning)}
    
    for pho in photo:
        count = 0
        for person in pho:
            count += score_map.get(person, 0)  # 이름이 없으면 기본값 0
        result.append(count)
    
    return result

from collections import Counter

def solution(clothes):
    # 의상 종류별로 개수 세기
    counter = Counter([category for _, category in clothes])
    
    # 조합의 수 계산 (각 카테고리별 의상 수 + 1(선택하지 않는 경우))
    combinations = 1
    for count in counter.values():
        combinations *= (count + 1)
    
    # 최소 하나는 입어야 하므로 아무것도 선택하지 않는 경우(1)를 제외
    return combinations - 1
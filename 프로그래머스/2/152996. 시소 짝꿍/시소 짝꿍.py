
3
4
5
6
7
8
9
10
11
12
13
14
15
16
from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0

    for c in counter:
        if counter[c] > 0:
            answer += counter[c] * (counter[c] - 1) // 2
            answer += counter[c] * counter[c * 4 / 3] # 4m & 3m
            answer += counter[c] * counter[c * 4 / 2] # 4m & 2m
            answer += counter[c] * counter[c * 3 / 2] # 3m & 2m

    return answer

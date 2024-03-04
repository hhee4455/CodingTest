def solution(n):
    array = []
    for i in range(n+1):
        if i % 2 != 0:
            array.append(i)
    return array
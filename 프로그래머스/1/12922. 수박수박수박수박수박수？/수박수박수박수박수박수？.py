def solution(n):
    suback = ["수", "박"]
    result = ""
    for i in range(n):
        result += suback[i % 2]
    return result

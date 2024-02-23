def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    return answer

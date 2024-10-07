def solution(x, n):

    # 제한조건 체크
    if not (-10000000 <= x <= 10000000):
        raise ValueError("x는 -10000000 이상, 10000000 이하의 정수여야 합니다.")
    if not (1 <= n <= 1000):
        raise ValueError("n은 1 이상, 1000 이하의 자연수여야 합니다.")
    
    answer = []
    for i in range(n):
        answer.append(x + x * i)
    return answer
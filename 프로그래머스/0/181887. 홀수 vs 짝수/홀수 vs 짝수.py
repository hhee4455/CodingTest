def solution(num_list):
    odd_sum = 0
    even_sum = 0

    for i, num in enumerate(num_list):
        if i % 2 == 0:  # 짝수 번째 인덱스
            even_sum += num
        else:
            odd_sum += num

    return max(odd_sum, even_sum)
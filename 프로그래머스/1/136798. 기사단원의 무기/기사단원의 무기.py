def solution(number, limit, power):
    total_sum = 0  

    def get_divisors_count(n):
        count = 0
        sqrt_n = int(n ** 0.5)
        for i in range(1, sqrt_n + 1):  
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count

    for num in range(1, number + 1):
        divisor_count = get_divisors_count(num)
        if divisor_count > limit:
            divisor_count = power
        total_sum += divisor_count  

    return total_sum

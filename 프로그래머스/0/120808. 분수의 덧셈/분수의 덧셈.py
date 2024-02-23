import math

def solution(numer1, denom1, numer2, denom2):
    numer_sum = numer1 * denom2 + numer2 * denom1
    denom_sum = denom1 * denom2
    
    gcd_value = math.gcd(numer_sum, denom_sum)
    
    numer_sum //= gcd_value
    denom_sum //= gcd_value
    
    return [numer_sum, denom_sum]
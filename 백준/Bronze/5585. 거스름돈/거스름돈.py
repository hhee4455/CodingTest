n = int(input())
count = 0
a = 1000-n

coin_types = [500,100,50,10,5,1]

for coin in coin_types:
    count += a // coin
    a %= coin

print(count)
a,b,c = map(int,input().split())
start_array = []
end_array = []
sum_pay = 0

for _ in range(3):
    m,n = map(int,input().split())
    start_array.append(m)
    end_array.append(n)

max_car = max(end_array)
pay_array = [0] * max_car

for index in range(start_array[0], end_array[0]):
    pay_array[index] += 1

for index in range(start_array[1], end_array[1]):
    pay_array[index] += 1

for index in range(start_array[2], end_array[2]):
    pay_array[index] += 1

for i in range(1,max_car):
    if pay_array[i] == 1:
        sum_pay += a
    elif pay_array[i] == 2:
        sum_pay += b * 2
    elif pay_array[i] == 3:
        sum_pay += c * 3

print(sum_pay)




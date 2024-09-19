import sys

n = int(sys.stdin.readline().rstrip())
num_list = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    num_list[num] += 1

for i in range(10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            sys.stdout.write(f'{i}\n')

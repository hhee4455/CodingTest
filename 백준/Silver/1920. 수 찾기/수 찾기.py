import sys

n = int(sys.stdin.readline())
num_n = set(map(int,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
num_m = list(map(int,sys.stdin.readline().strip().split()))


for num in num_m:
    if num in num_n:
        sys.stdout.write(str(1) + '\n')
    else:
        sys.stdout.write(str(0) + '\n')
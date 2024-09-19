import sys
n = int(sys.stdin.readline().strip())
channel_array = [sys.stdin.readline().strip() for _ in range(n)]
idx1, idx2 = channel_array.index("KBS1"), channel_array.index("KBS2")
if idx1 > idx2:
    idx2+=1

print('1'*idx1 + '4'*idx1 + '1'*idx2 + '4'*(idx2-1))
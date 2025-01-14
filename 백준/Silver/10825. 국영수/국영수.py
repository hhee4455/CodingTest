n = int(input())
input_array = []

for i in range(n):
    name, kr, en, ma = input().split()
    input_array.append((name,int(kr),int(en),int(ma)))

array = sorted(input_array, key=lambda x:(-x[1],x[2],-x[3],x[0]))

for name in array:
    print(name[0])
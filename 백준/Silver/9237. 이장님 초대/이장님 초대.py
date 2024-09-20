n = int(input())
tree = list(map(int,input().split()))

tree.sort(reverse=True)

for i in range(n):
    tree[i] += i
    
tree_max = max(tree)

print(tree_max+2)
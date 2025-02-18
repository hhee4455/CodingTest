def soultion(g,game):
    name = set(game)
    if g =="Y":
        a = 1
    elif g =="F":
        a = 2
    else:
        a = 3 
    
    return len(name) // a







n, g = input().split()
game = [input() for _ in range(int(n))]

print(soultion(g,game))
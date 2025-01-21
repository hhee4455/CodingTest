def solution(park, routes):
    for i, row in enumerate(park):
        if "S" in row:
            y, x = i, row.index("S")
            break
    
    max_y = len(park)
    max_x = len(park[0])

    for route in routes:
        op, n = route.split(" ")
        n = int(n)
        dx, dy = x, y
        
        for _ in range(n):
            if op == "N":
                dy -= 1
            elif op == "S":
                dy += 1
            elif op == "W":
                dx -= 1
            elif op == "E":
                dx += 1
            
            if dy < 0 or dy >= max_y or dx < 0 or dx >= max_x or park[dy][dx] == "X":
                dx, dy = x, y
                break
        
        x, y = dx, dy

    return [y, x]

def find_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    x = int(data[0])
    y = int(data[1])
    
    quadrant = find_quadrant(x, y)
    print(quadrant)

if __name__ == "__main__":
    main()

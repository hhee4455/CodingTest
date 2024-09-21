import sys

array = []

def add(x):
    x = int(x)
    if x not in array:
        array.append(x)

def remove(x):
    x = int(x)
    if x in array:
        array.remove(x)

def check(x):
    x = int(x)
    if x in array:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")

def toggle(x):
    x = int(x)
    if x in array:
        array.remove(x)
    else:
        array.append(x)

def alll(x):
    global array
    array = [i for i in range(1, 21)]

def empty(x):
    global array
    array = []

m = int(sys.stdin.readline())

for i in range(m):
    cal, *x = sys.stdin.readline().rstrip().split()
    x = x[0] if x else 0
    if cal == "add":
        add(x)
    elif cal == "remove":
        remove(x)
    elif cal == "check":
        check(x)
    elif cal == "toggle":
        toggle(x)
    elif cal == "all":
        alll(x)
    elif cal == "empty":
        empty(x)

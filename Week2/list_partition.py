def list_partition():
    n, x, y = map(int, input("Enter values n, x, y : ").split())
    if (x+y) != n:
        print("x + y != n")
    else:
        lt = list(map(int, input("Enter spaced integers: ").split()))
        lt.sort()
        p = lt[y] - lt[y-1] -1
        print("Count = ", p)
list_partition()

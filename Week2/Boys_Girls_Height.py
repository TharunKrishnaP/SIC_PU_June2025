#Boys Girls Height
t = int(input("Enter no. of test cases: "))
def height_append(a,b):
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if i==0:
            height_order.append(a[i])
        else:
            last = height_order[-1]
            if i%2==0:
                if last not in a:
                    if a[i] > last:
                        height_order.append(a[i])
                        i += 1
            elif i%2!=0:
                if last not in b:
                    if b[j] > last:
                        height_order.append(b[j])
                        j += 1

for i in range(1,t+1):
    print(f"Test case {i}")
    n = int(input("Class strength: "))
    print(f" Boys = Girls = {n//2}")
    b = list(map(int, input("Enter boys height : ").split()))
    g = list(map(int, input("Enter girls height : ").split()))
    b.sort()
    g.sort()
    height_order = []
    if b[0] < g[0]:
        height_append(b,g)
    else:
        height_append(g,b)
    print(height_order)
    if len(height_order) == n:
        print("Yes")
    else:
        print("No")
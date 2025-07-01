#Boys Girls Height
t = int(input("Enter no. of test cases: "))
def height_append(a,b):
    i = j = k = 0
    while (i<len(a) or j<len(b)) and k<n:
        if k==0:
            height_order.append(a[i])
            k += 1
        else:
            last = height_order[-1]
            if k%2==0:
                while i < len(a) and a[i] <= last:
                    i += 1
                if i <len(a) and a[i] > last:
                    height_order.append(a[i])
                    i += 1
            elif k%2!=0:
                while j < len(b) and b[j] <= last:
                    j += 1
                if j<len(b) and b[j] > last:
                    height_order.append(b[j])
                    j += 1
            k +=1

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
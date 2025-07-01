#Boys Girls Height
t = int(input("Enter no. of test cases: "))
def height_append(a,b):
    i = j = k = 0
    while (i<len(a) or j<len(b)) and k<class_strength:
        if k==0:
            height_order.append(a[i])
            k += 1
        else:
            last = height_order[-1]
            if k%2==0:
                while i < len(a) and a[i] < last:
                    i += 1
                if i <len(a) and a[i] >= last:
                    height_order.append(a[i])
                    i += 1
            elif k%2!=0:
                while j < len(b) and b[j] < last:
                    j += 1
                if j<len(b) and b[j] >= last:
                    height_order.append(b[j])
                    j += 1
            k +=1
    if len(height_order) == class_strength:
        print("Yes")
    else:
        print("No")

for i in range(1,t+1):
    print(f"Test case {i}")
    class_strength = int(input("Class strength: "))
    print(f" Boys = Girls = {class_strength//2}")
    boys = list(map(int, input("Enter boys height : ").split()))
    girls = list(map(int, input("Enter girls height : ").split()))
    boys.sort()
    girls.sort()
    height_order = []
    if boys[0] < girls[0]:
        height_append(boys,girls)
    else:
        height_append(girls,boys)
    print(height_order)

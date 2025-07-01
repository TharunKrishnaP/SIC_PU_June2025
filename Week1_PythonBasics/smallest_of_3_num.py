#Smallest of 3 distinct numbers
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
if a<b and a<c:
    print("Smallest: ",a)
elif b<a and b<c:
    print("Smallest: ",b)
else:
    print("Smallest: ",c)
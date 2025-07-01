#Hollow Square
n = int(input("Enter no. of lines: "))
print("# "*n)
for i in range(1,n-1):
    print("# " + "  "*(n-2) + "#")
print("# "*n)
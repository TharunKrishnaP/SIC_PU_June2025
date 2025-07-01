#Right Angled Triangle
n = int(input("Enter no. of lines: "))
for i in range(n):
    print("|" + " "*i + "\\")
    if i==(n-1):
        print("|" + "_"*(i+1) + "\\")
n = int(input("Enter no. of lines: "))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
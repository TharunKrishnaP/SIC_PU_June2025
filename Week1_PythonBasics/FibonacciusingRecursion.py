def fibonacci(n, a=1, b=2,count=0):
    if count<n:
        return fibonacci(n, b, a + b,count+1)
    else:
        return a
n = int(input("Enter term no. : "))
a = fibonacci(n-1)
print(a)
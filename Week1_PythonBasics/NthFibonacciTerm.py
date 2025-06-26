# Nth Fibbonacci term
term = int(input("Enter the term no. : "))
a = 1
b = 2
for i in range(2,term):
    a , b = b , a+b
print(f"Term no. {term} in Fibbonacci Series is {a}.")
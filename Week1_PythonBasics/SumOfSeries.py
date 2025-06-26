# Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
n = int(input("Value of n: "))
m = int(input("No of terms: "))
sum_of_series = 0
for i in range(m):
    term = (n**2**i)/(2*i+1)
    if i%2==0:
        sum_of_series += term
    else:
        sum_of_series -= term
print(f"Sum of given series: {sum_of_series}")
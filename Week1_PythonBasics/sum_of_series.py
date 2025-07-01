# Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
n = int(input("Value of n: "))
m = int(input("No of terms: "))
sum_of_series = 0
for i in range(m):
    numerator = (n**2**i)
    denominator = (2*i+1)
    sign = (-1)**i
    term = numerator / denominator * sign
    sum_of_series += term
print(f"Sum of given series: {sum_of_series}")
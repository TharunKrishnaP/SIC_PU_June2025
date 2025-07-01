# 2nd smallest digit in a number using loops
number = int(input("Enter number: "))
lt = []
for i in str(number):
    lt.append(int(i))
lt = sorted(set(lt))
print(f"2nd smallest digit of {number} is {lt[1]}")
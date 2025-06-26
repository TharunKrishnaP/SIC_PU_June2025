#Biggest digit of a number using loops
num = int(input("Enter number: "))
max_digit = 0
for i in str(num):
    if int(i) > max_digit:
        max_digit = int(i)
print(f"Biggest Digit of {num} is {max_digit}")
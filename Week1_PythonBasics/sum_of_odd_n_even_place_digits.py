# Sum of odd placed digits and even placed digits of a number
number = input("Enter number: ")
odd_sum = 0
even_sum = 0
for i in range(len(number)):
    x = int(number[i])
    if i%2!=0:                            # If the index is assumed to start from 1.
        even_sum += x
    else:
        odd_sum += x
print(f"Sum of odd placed digits: {odd_sum}")
print(f"Sum of even placed digits: {even_sum}")
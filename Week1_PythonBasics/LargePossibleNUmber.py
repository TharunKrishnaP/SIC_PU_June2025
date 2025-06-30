input_num = input("Enter number: ")
num_lt = [i for i in str(input_num)]
num_lt = sorted(input_num, reverse=True)
large_num = "".join(num_lt)
print(f"Largest possible number from digits of given number: {large_num}")
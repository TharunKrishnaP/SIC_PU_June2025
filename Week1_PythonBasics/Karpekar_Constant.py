def Karpekar_Constant(num,count=0):
    num_str = f"{int(num):04d}"
    asc_num = int("".join(sorted(num_str)))
    desc_num = int("".join(sorted(num_str,reverse=True)))
    diff = desc_num - asc_num
    print(f"{desc_num:4} - {asc_num:4} = {diff:4}")
    count += 1
    if diff != 6174:
        return Karpekar_Constant(diff,count)
    return count

print("Input must be a 4-digit number where a digit can repeat utmost 2 times")
input_num = input("Enter number: ")
count = Karpekar_Constant(input_num)
print(f"Number {input_num} took {count} iterations to reach Karpekar Constant 6174")
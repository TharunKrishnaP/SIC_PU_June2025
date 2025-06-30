try:
    numbers = [float(num) for num in input().split()]
    print(numbers)
except ValueError:
    print("Kindly check your input.")
    print("-------Exit-----------")
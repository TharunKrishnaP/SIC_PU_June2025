lt = list(map(int, input("Enter spaced integers: ").split()))
lt.sort()
print(f"Smallest Element: {lt[0]}")
print(f"Largest Element: {lt[-1]}")
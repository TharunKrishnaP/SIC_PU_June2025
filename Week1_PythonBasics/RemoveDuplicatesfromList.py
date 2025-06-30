lt = list(map(int, input("Enter spaced integers: ").split()))
new_lt = []
for i in lt:
    if i not in new_lt:
        new_lt.append(i)
print(f"After removing duplicates from list: \n {new_lt}")
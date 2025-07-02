# Improvised Bubble sort
list1 = list(map(int, input().split()))
n = len(list1)
count = 0
for i in range(n):
    sorted = True
    for j in range(n-i-1):
        if list1[j+1] < list1[j]:
            min_element = list1[j+1]
            list1[j+1] = list1[j]
            list1[j] = min_element
            count += 1
            sorted = False
    if sorted:
        break
print(list1)
print(f"No of iterations: {count}")
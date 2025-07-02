# Linear Search
elements_list = list(map(int, input().split()))
key = int(input())
for i in elements_list:
    if key == i:
        print("Key found")
    else:
        print("Key Not found")
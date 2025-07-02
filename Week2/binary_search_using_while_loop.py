# Binary search using while
elements_list = list(map(int, input().split()))
elements_list.sort()
key = int(input())
left = 0
right = len(elements_list) -1
while left <= right:
    mid = (left + right)//2
    if elements_list[mid] == key:
        print(f"Key found at index {mid}")
        break
    elif elements_list[mid] < key:
        left = mid+1
    else:
        right = mid-1
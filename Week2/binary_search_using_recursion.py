# Binary search using recursion
def binary_search(left , right):
    mid = (left + right)//2
    if elements_list[mid] == key:
        print(f"Key found at index {mid}")
    elif elements_list[mid] <key:
        binary_search(left , right=mid-1)
    else:
        binary_search(right , left = mid+1)
elements_list = list(map(int, input().split()))
key = int(input())
left = 0
right = len(elements_list) - 1
binary_search(left,right)
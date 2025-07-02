#Orange Partition
#Quick Sort algorithm
def quicksort(array, low, high):
    if low<high:
        pivot_index = Partition(array, low, high)
        quicksort(array, low, pivot_index -1)
        quicksort(array, pivot_index+1, high)

def Partition(array, low, high):
    pivot = array[high]
    k = low
    for i in range(low,high):
        if array[i] < pivot:
            array[i] , array[k] = array[k] , array[i]
            k+=1
    array[k] , array[high] = array[high] , array[k]
    return k

orange_list = list(map(int, input().split()))
low = 0
high = len(orange_list) -1
quicksort(orange_list, low, high)
print(orange_list)
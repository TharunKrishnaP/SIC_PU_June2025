no_of_elements_A = int(input())
list_A = list(map(int, input().split()))
no_of_elements_B = int(input())
list_B = list(map(int, input().split()))
freq_A = {}
freq_B = {}
for num in list_A:
    if num in freq_A:
        freq_A[num] += 1
    else:
        freq_A[num] = 1
for num in list_B:
    if num in freq_B:
        freq_B[num] += 1
    else:
        freq_B[num] = 1
missing = []
for num in freq_B:
    if freq_B[num] > freq_A.get(num, 0):
        missing.append(num)
missing.sort()
for i in missing:
    print(i, end = " ")
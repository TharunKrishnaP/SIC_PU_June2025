no_of_request = int(input("No of requests: "))
requests = list(map(int, input("Enter spaced integers: ").split()))
server1 = requests[:(no_of_request):2]
server2 = requests[1:(no_of_request):2]
allocated_mem_s1 = 0
deallocated_mem_s1 = 0
allocated_mem_s2 = 0
deallocated_mem_s2 = 0
for i in server1:
    if i>0:
        allocated_mem_s1 += i
    else:
        deallocated_mem_s1 += abs(i)
for i in server2:
    if i>0:
        allocated_mem_s2 += i
    else:
        deallocated_mem_s2 += abs(i)

print("Server 1")
print(f"Allocated Memory: {allocated_mem_s1}")
print(f"De-allocated Memory: {deallocated_mem_s1}")

print("Server 2")
print(f"Allocated Memory: {allocated_mem_s2}")
print(f"De-allocated Memory: {deallocated_mem_s2}")
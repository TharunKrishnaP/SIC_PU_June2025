no_of_request = int(input("No of requests: "))
requests = list(map(int, input("Enter spaced integers: ").split()))
server1 = requests[:(no_of_request):2]
server2 = requests[1:(no_of_request):2]
allocated_mem_s1 = sum(server1)
allocated_mem_s2 = sum(server2)

print("Server 1")
print(f"Allocated Memory: {allocated_mem_s1} units")

print("Server 2")
print(f"Allocated Memory: {allocated_mem_s2} units")

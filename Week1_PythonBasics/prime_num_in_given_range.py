# Print the Prime numbers in decreasing order between m and n (m < n)
m ,n = map(int, input("Enter values for m and n as spaced integers: ").split())
prime = []
not_prime = []
for i in range(m,n):
    i = int(i)
    if i==0 or i==1:
        not_prime.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                not_prime.append(i)
                break
        else:
            prime.append(i)
print(f"Prime numers in given range ({m},{n})")
for i in prime[::-1]:
    print(i, end = " ")
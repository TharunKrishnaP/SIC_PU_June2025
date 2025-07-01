#Count of Prime numbers in given number
input_num = int(input("Enter number: "))
prime = []
not_prime = []
for i in str(input_num):
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
print(f"Count of Prime numbers in given number is {len(prime)}")
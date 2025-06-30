lt = list(map(int, input("Enter spaced integers: ").split()))
count = {}
for i in set(lt):
    count[i] = lt.count(i)
print("Frequency of Elements:")
for key , value in count.items():
    print(f" {key} : {value}")
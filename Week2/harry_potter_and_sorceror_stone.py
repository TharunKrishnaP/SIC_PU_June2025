gold_coin_Harry_bag = int(input())
worth_of_goldcoins = list(map(int, input().split()))
no_of_instructions , X = map(int, input().split())
monk_bag = []
for i in range(no_of_instructions):
    str = input()
    if str == "Harry":
        temp = worth_of_goldcoins[0]
        del worth_of_goldcoins[0]
        monk_bag.append(temp)
    elif str == "Remove":
        monk_bag.pop()
    if sum(monk_bag) == X:
        print(len(monk_bag))
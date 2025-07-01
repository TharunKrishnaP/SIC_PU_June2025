test_cases = int(input())
for i in range(test_cases):
    N , start = map(int, input().split())
    ID = []
    ID.append(start)
    for i in range(N):
        turn = input().strip("P ")
        if turn=="B":
            ID.append(ID[-2])
        else:
            player_id = int(turn)
            ID.append(player_id)
    print("Player",ID[-1])
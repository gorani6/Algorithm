game_count = int(input())
y_win = 0
k_win = 0

for i in range(game_count):
    k_score = 0
    y_score = 0
    for j in range(9):
        y, k = map(int, input().split())
        k_score += k
        y_score += y

    if k_score > y_score:
        k_win += 1
    elif y_score > k_score:
        y_win += 1

    k_score *= 0
    y_score *= 0

    if y_win > k_win:
        print('Yonsei')
    elif k_win > y_win:
        print('Korea')
    else:
        print('Draw')
    y_win *= 0
    k_win *= 0

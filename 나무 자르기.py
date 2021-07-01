import sys

cnt, cut_line = map(int, sys.stdin.readline().split())
tree_ = list(map(int, sys.stdin.readline().split()))

left = 1
right = 2000000000
suss = 0
while left <= right:
    middle = (left + right) // 2
    for i in range(cnt):
        if tree_[i] - middle > 0:
            suss += tree_[i] - middle
    if suss >= cut_line:
        left = middle + 1
    elif suss < cut_line:
        right = middle - 1

    suss = 0

print(left-1)

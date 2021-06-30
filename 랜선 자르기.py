K, N = map(int, input().split())
list1 = []

for i in range(K):
    x = int(input())
    list1.append(x)
list1.sort()
left = 1
right = 2 ** 31 - 1
cnt = 0

while left <= right:
    middle = (left + right) // 2
    for j in range(len(list1)):
        cnt += list1[j] // middle
    print(cnt, middle, left, right)
    if cnt < N:
        right = middle - 1
    elif cnt >= N:
        left = middle + 1
    cnt = 0

print(left-1)
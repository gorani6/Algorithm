import sys
N = int(input())
counting_list = [0] * 10001

for i in range(N):
    n = int(sys.stdin.readline())
    counting_list[n] += 1

for j in range(1, 10001):
    count = counting_list[j]
    for _ in range(count):
        print(j)
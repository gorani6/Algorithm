li = [0, 1, 3]

for i in range(3, 1001):
    li.append(li[i-2]*2 + li[i-1])

n = int(input())
print(li[n]%10007)
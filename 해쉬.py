D = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
     'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
     'x': 24, 'y': 25, 'z': 26}

n = int(input())
s = input()
n2_ = list(range(1, n+1))
list1 = []
for i in s:
    if i in D:
        list1.append(D.get(i))
list2 = []
for j in range(n):
    list2.append(list1[j] * 31** j)

print(sum(list2)%1234567891)

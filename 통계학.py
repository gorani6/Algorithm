from collections import Counter
import sys
cnt = int(sys.stdin.readline())
list1 = []
for i in range(cnt):
    num = int(sys.stdin.readline())
    list1.append(num)
print(round(sum(list1)/len(list1)))
list1.sort()
a = len(list1)/2
a = int(a)
print(list1[a])

list2 = Counter(list1)
list2 = sorted(list2.items(), key=lambda x: (-x[1],x[0]))
if len(list1) == 1:
    print(list1[0])
elif list2[0][1] == list2[1][1]:
    print(list2[1][0])
else:
    print(list2[0][0])

print(list1[-1] - list1[0])

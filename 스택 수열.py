cnt = int(input())
list1 = []
list2 = []
num = 1
flag = True

for i in range(cnt):
    n = int(input())
    while num <= n:
        list1.append(num)
        list2.append('+')
        num += 1
    if list1[-1] == n:
        list1.pop()
        list2.append('-')
    else:
        flag = False
if flag == False:
    print('NO')
else:
    for i in list2:
        print(i)
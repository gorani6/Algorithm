list1 = [0, 1]
x = int(input())

for i in range(2, x+1):
    list1.append(list1[i - 1] + list1[i - 2])

print(list1[x])
s = int(input())
li = [1]
i = 1
while s >= 0:
    if s == 1:
        li.append(1)
        break
    s -= i
    li.append(i)
    i += 1

print(li[-2])
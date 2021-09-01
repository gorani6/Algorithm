li = []
while True:
    cuntDay = 0
    L, P, V = map(int, input().split())
    if L == 0:
        break
    else:
      if V % P >= L:
          cuntDay += (V // P) * L + L
      else:
          cuntDay += (V // P) * L + V - (V // P * P)
    li.append(cuntDay)

for i in range(0, len(li)):
    print("Case " +str(i+1)+ ":",li[i])

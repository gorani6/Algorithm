s = list(input())

li_cnt = []
sum_cnt = 0
for i in range(len(s)):
    cnt = 0
    if s[i] == "(" and s[i+1] == ")":
        cnt += len(li_cnt)
        cnt += -1

    if s[i] == '(':
        li_cnt.append("(")
    elif s[i] == ")":
        li_cnt.pop()
        cnt += 1

    sum_cnt += cnt

print(sum_cnt)

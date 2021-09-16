N, M = map(int, input().split())

cnt = 0

six_string_price = []
string_price = []
for i in range(M):
    n, m = map(int, input().split())
    six_string_price.append(n)
    string_price.append(m)

if min(six_string_price) < min(string_price) * 6:
    if min(six_string_price) < min(string_price) * (N % 6):
        cnt = (N // 6 + 1) * min(six_string_price)
    else:
        cnt = N // 6 * min(six_string_price) + N % 6 * min(string_price)

elif min(six_string_price) >= min(string_price) * 6:
    cnt = N*min(string_price)

print(cnt)

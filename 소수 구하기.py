def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

m, n = map(int, input().split())

for x in range(m, n+1):
    if is_prime(x):
        print(x)

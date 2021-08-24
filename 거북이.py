N = list(map(int, input().split()))
N.sort()
N1 = min(N[0], N[1])
N2 = min(N[2], N[3])

print(N1 * N2)
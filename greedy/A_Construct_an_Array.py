t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for i in range(1, 2 * n + 1, 2):
        res.append(i)
    print(*res)
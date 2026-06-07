t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    res = []
    for i in range(2, n):
        if a[i] != a[i - 2]  % a[i - 1]:
            res = [-1]
            break
    if res:
        print(*res)
    else:
        print(*a[:2])
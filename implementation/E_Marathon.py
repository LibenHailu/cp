t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    ans = 0
    if a < b:
        ans += 1
    if a < c:
        ans += 1
    if a < d:
        ans += 1
    print(ans)
    
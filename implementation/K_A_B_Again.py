t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    while n:
        res += n % 10
        n //= 10
    print(res)  
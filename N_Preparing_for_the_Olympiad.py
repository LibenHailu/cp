t = int(input())
for _ in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    total = sum(a)
    for x in b:
        if x in a:
            continue
        else:
            total -= x
    print(total)

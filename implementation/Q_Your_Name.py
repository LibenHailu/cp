t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split(" ")
    # print(a)
    b, c = sorted(list(a[0])), sorted(list(a[1]))
    # print(b, c)
    if (b == c):
        print("YES")
    else:
        print("NO")
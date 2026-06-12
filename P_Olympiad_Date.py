for _ in range(int(input())):
    n = int(input())
    count = {
        0: 3, 
        1: 1,
        2: 2, 
        3:1,
        5:1
    }
    cur = {}
    a = list(map(int, input().split()))
    found = False
    for j, i in enumerate(a):
        if i in count and cur.get(i, 0) < count[i]:
            cur[i] = 1 + cur.get(i, 0)
        if cur == count:
            found = True
            print(j + 1)
            # print(n, cur, count)   
            break
    if not found:
        print(0)
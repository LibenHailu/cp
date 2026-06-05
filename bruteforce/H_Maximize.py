import math


t = int(input())
for _ in range(t):
    n = int(input())
    cur_max = 0
    cur_y = 0
    for y in range(1, n):
        if cur_max < math.gcd(n, y) + y:
            cur_max = math.gcd(n, y) + y
            cur_y = y
    print(cur_y)
from typing import Counter


t = int(input())
for _ in range(t):
    n = int(input())    
    s = input()
    count = Counter(s)
    res = 0
    for k, v in count.items():
        res +=  2
        res += v  - 1
    print(res)
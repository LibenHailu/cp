import math


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
   
    diff = abs(a  - b)
    print(math.ceil(diff/10))
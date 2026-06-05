t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 and k % 2 == 0 or n < k:
        print("NO")
    else:
        print("YES")    

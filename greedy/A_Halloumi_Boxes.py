t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if arr == sorted(arr):
        print("YES")    
    
    elif k >= 2:
        print("YES")
    
    else:
        print("NO")
    
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    max_val = max(a)
    total = sum(a)
    print(max_val - (total - max_val))
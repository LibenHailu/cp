t = int(input())

for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())

    x = a1 + a2     
    y = a4 - a2      
    z = a5 - a4     

    vals = [x, y, z]

    answer = max(vals.count(x), vals.count(y), vals.count(z))

    print(answer)


    
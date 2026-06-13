import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        
        if n == 2:
            results.append("2")
        elif n % 2 == 0:
            results.append("0")
        else:
            results.append("1")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
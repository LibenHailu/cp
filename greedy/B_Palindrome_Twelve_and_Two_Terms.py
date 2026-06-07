# all = []
# def find_palidrome(i, cur):
#     if i == 9:
#         return 
#     if cur:
#         all.append(int(cur))
#     for j in range(9):
#         find_palidrome(i + 1, str(j) + cur + str(j))

# for i in range(1, 10):
#     find_palidrome(1, str(i))
#     find_palidrome(1, str(i) * 2)

# print(all)

        
# for _ in range(int(input())):
#     n = int(input())
#     # find_palidrome()
#     # l, r = map(int, input().split())
#     # if not all:
#     #     find_palidrome()
#     # res = []
#     # for i in all:
#     #     if l <= i <= r:
#     #         res.append(i)
#     # print(*res)
# all = []
# def find_palidrome(i, cur):
#     if i == 9:
#         return 
#     if cur:
#         all.append(int(cur))
#     for j in range(9):
#         find_palidrome(i + 1, str(j) + cur + str(j))

# for i in range(1, 10):
#     find_palidrome(1, str(i))
#     find_palidrome(1, str(i) * 2)

# print(all)

        
# for _ in range(int(input())):
#     n = int(input())
#     # find_palidrome()
#     # l, r = map(int, input().split())
#     # if not all:
#     #     find_palidrome()
#     # res = []
#     # for i in all:
#     #     if l <= i <= r:
#     #         res.append(i)
#     # print(*res)
# import sys

# def solve():
#     input = sys.stdin.read
#     data = input().split()
#     if not data:
#         return
    
#     t = int(data[0])
#     results = []
    
#     for i in range(1, t + 1):
#         n = int(data[i])
#         found = False
        
#         # Strategy 1: Check if b is a small multiple of 12
#         for k in range(2001):
#             b = k * 12
#             if b > n:
#                 break
#             a = n - b
#             s_a = str(a)
#             if s_a == s_a[::-1]:
#                 results.append(f"{a} {b}")
#                 found = True
#                 break
                
#         if found:
#             continue
            
#         # Strategy 2: Construct a palindrome matching n's length
#         s_n = str(n)
#         length_n = len(s_n)
        
#         # Try lengths from length_n - 1 to length_n
#         for length in range(max(1, length_n - 1), length_n + 1):
#             if found:
#                 break
#             # Try baseline repdigits '1' and '2'
#             for base_char in ['1', '2']:
#                 if found:
#                     break
                
#                 mid1 = (length - 1) // 2
#                 mid2 = length // 2
                
#                 # Tweak the middle digit(s)
#                 for mid_digit in range(10):
#                     a_list = [base_char] * length
#                     a_list[mid1] = str(mid_digit)
#                     a_list[mid2] = str(mid_digit)
                    
#                     a = int("".join(a_list))
                    
#                     if a <= n and (n - a) % 12 == 0:
#                         results.append(f"{a} {n - a}")
#                         found = True
#                         break
                        
#         if not found:
#             results.append("-1")
            
#     print("\n".join(results))

# if __name__ == '__main__':
#     solve()
import sys

def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    # Precomputing 10^i % 12 for up to 20 digits
    pow10mod = [0] * 20
    pow10mod[0] = 1
    for i in range(1, 20):
        pow10mod[i] = (pow10mod[i - 1] * 10) % 12

    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        if idx >= len(data):
            break
        n = int(data[idx])
        idx += 1
        
        s = str(n)
        length = len(s)
        target = n % 12
        found = False
        ans = -1
        
        # Iterating from the maximum possible length down to 1
        for m in range(length, 0, -1):
            if found:
                break
            
            bound = (m == length)
            h = (m + 1) // 2
            digit = [0] * m
            
            # DP/Memoization table initialized to -1 (meaning unvisited)
            # Shapes: bad[pos][mod][tight]
            bad = [[[-1 for _ in range(2)] for _ in range(12)] for _ in range(h + 1)]
            
            limit_pal = list(s)
            bound_pal_ok = True
            
            if bound:
                for i in range(h):
                    limit_pal[m - 1 - i] = limit_pal[i]
                bound_pal_ok = ( "".join(limit_pal) <= s )
            
            def dfs(pos, current_mod, tight):
                if pos == h:
                    if current_mod != target:
                        return False
                    if bound and tight and not bound_pal_ok:
                        return False
                    return True
                
                # Check memoization cache
                if bad[pos][current_mod][1 if tight else 0] == 0:
                    return False
                
                lim = 9
                if bound and tight:
                    lim = int(s[pos])
                
                start = 0
                if pos == 0 and m > 1:
                    start = 1
                
                right = m - 1 - pos
                coeff = pow10mod[right]
                if right != pos:
                    coeff = (coeff + pow10mod[pos]) % 12
                
                for d in range(start, lim + 1):
                    digit[pos] = d
                    digit[right] = d
                    
                    ntight = bound and tight and (d == lim)
                    nmod = (current_mod + d * coeff) % 12
                    
                    if dfs(pos + 1, nmod, ntight):
                        return True
                
                # Mark this state as failed (0 means bad state)
                bad[pos][current_mod][1 if tight else 0] = 0
                return False

            if dfs(0, 0, bound):
                # Convert digit array to integer
                ans = int("".join(map(str, digit)))
                found = True
        
        if not found:
            out.append("-1")
        else:
            out.append(f"{ans} {n - ans}")
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    # Increase recursion depth just in case, though max depth here is small (h <= 10)
    sys.setrecursionlimit(2000)
    solve()
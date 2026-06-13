import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        x = int(data[idx + 2])
        idx += 3

        va = []
        cnt = 0
        while True:
            va.append((a, cnt))
            if a == 0:
                break
            a //= x
            cnt += 1

        vb = []
        cnt = 0
        while True:
            vb.append((b, cnt))
            if b == 0:
                break
            b //= x
            cnt += 1

        best = float("inf")

        for val_a, div_a in va:
            for val_b, div_b in vb:
                best = min(
                    best,
                    div_a + div_b + abs(val_a - val_b)
                )

        ans.append(str(best))

    print("\n".join(ans))

if __name__ == "__main__":
    solve()
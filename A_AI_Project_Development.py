t = int(input())

for _ in range(t):
    n, x, y, z = map(int, input().split())

    no_ai = (n + (x + y) - 1) // (x + y)

    finish_during_setup = (n + x - 1) // x

    if finish_during_setup <= z:
        with_ai = finish_during_setup
    else:
        remaining = n - x * z
        with_ai = z + (remaining + (x + 10 * y) - 1) // (x + 10 * y)

    print(min(no_ai, with_ai))
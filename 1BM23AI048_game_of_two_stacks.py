print("question: Game of Two Stacks\nname:C Disha\nUSN: 1BM23AI048\nsec:3A")
x = int(input())
for i in range(x):
    n, m, max_sum = input().split()
    n = int(n)
    m = int(m)
    max_sum = int(max_sum)
    a = input().split()
    l1 = []
    for j in range(n):
        l1.append(int(a[j]))
    b = input().split()
    l2 = []
    for j in range(m):
        l2.append(int(b[j]))
    u = [0] * (n + 1)
    for j in range(1, n + 1):
        u[j] = u[j - 1] + l1[j - 1]
    v = [0] * (m + 1)
    for j in range(1, m + 1):
        v[j] = v[j - 1] + l2[j - 1]
    count = 0
    p = m
    for o in range(n + 1):
        if u[o] > max_sum:
            break
        while p > 0 and (u[o] + v[p] > max_sum):
            p -= 1
        count = max(count, o + p)
    print(count)

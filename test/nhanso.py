def mu(n, m):
    if m == 0:
        return 1
    if m % 2 != 0:
        return mu(n, m // 2) * mu(n, m // 2) * n
    return mu(n, m // 2) * mu(n, m // 2)

print(mu(2, 100))

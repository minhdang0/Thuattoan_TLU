def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = min(len(str(x)), len(str(y)))
    m = n // 2

    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((high_x + low_x), (high_y + low_y))
    z2 = karatsuba(high_x, high_y)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

x = 1234
y = 5678
result = karatsuba(x, y)
print(f"Kết quả của phép nhân {x} và {y} bằng thuật toán Karatsuba là:: {result}")

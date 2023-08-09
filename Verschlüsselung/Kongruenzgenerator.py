def linear_generator(m, a, c, x0, count, cut):
    k = []
    x = x0
    for _ in range(count):
        k.append(x//2**cut)
        x = (a*x + c) % m
    return k



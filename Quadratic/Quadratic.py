def discriminant(a, c, b):
    return 4*a*c+b**2


def quadratic(a, c, b):
    if a == 0:
        return ()
    d = discriminant(a, c, b)
    if d < 0:
        return ()
    return (-b + d ** (1 / 2)) / 2 * a, (-b - d ** (1 / 2)) / 2 * a

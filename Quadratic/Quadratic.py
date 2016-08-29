from math import sqrt


class Quadratic(object):
    def result(self, a, b, c):
        pass


class NormalQuadratic(Quadratic):
    def result(self, a, b, c):
        if a == 0:
            return ()
        d = NormalQuadratic.discriminant(a, b, c)
        if d < 0:
            return ()
        return (-b + sqrt(d)) / 2 * a, (-b - sqrt(d)) / 2 * a

    @staticmethod
    def discriminant(a, b, c):
        return b ** 2 - 4 * a * c


class SecondQuadratic(Quadratic):
    def result(self, a, b, c):
        if a == 0:
            return ()
        d = b ** 2 - 4 * a * c
        if d < 0:
            return ()
        return (-b + sqrt(d)) / 2 * a, (-b - sqrt(d)) / 2 * a


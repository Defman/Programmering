class Quadratic(object):
    def result(self, a, b, c):
        pass


class NormalQuadratic(Quadratic):
    def result(self, a, b, c):
        if a == 0:
            return ()
        d = NormalQuadratic.discriminant(a, c, b)
        if d < 0:
            return ()
        return (-b + d ** (1 / 2)) / 2 * a, (-b - d ** (1 / 2)) / 2 * a

    @staticmethod
    def discriminant(a, c, b):
        return 4 * a * c + b ** 2


class SecondQuadratic(Quadratic):
    def result(self, a, b, c):
        if a == 0:
            return ()
        d = 4 * a * c + b ** 2
        if d < 0:
            return ()
        return (-b + d ** (1 / 2)) / 2 * a, (-b - d ** (1 / 2)) / 2 * a


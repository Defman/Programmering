from unittest import TestCase
from Quadratic import NormalQuadratic, SecondQuadratic
from numpy import random

class TestNormalQuadratic(TestCase):
    def test_quadratic(self):
        normal = NormalQuadratic()
        second = SecondQuadratic()

        test = [random.rand(3) for x in range(9)]

        i1 = []
        i2 = []

        for a, b, c in test:

            r1 = normal.result(a, b, c)


            r2 = second.result(a, b, c)

            self.assertEqual(, )

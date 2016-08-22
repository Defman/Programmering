from unittest import TestCase
import Quadratic


class TestQuadratic(TestCase):
    def test_quadratic(self):
        self.assertEqual(Quadratic.quadratic(1, 2, 3), (0.5615528128088303, -3.5615528128088303))

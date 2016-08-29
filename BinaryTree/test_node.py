from unittest import TestCase
from BinaryTree import Node
import numpy as np


class TestNode(TestCase):
    def test_insert_search(self):
        keys = np.random.rand(200) * 10
        values = np.random.rand(200) * 100

        root = Node(keys[0], values[0])
        print("Inserted value", values[0], "at", keys[0])
        for key, value in zip(keys[1:], values[1:]):
            root.insert(key, value)
            print("Inserted value", value, "at", key)

        for key, value in zip(keys, values):
            result = root.search(key)
            print("Found value", result, "at", key)
            self.assertEqual(value, result, "Error")
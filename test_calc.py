import unittest
from calc import add, subtract, multiply, divide

class TestCalc(unittest.TestCase):
    def setUp(self):
        """Set up test variables"""
        self.num1 = 3
        self.num2 = 2

    def test_add(self):
        self.assertEqual(add(self.num1, self.num2), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(self.num1, self.num2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(self.num1, self.num2), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(self.num1, self.num2), 1.5)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()

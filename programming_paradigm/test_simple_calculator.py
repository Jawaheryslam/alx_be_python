import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()


    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 5), 5)


    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        self.assertEqual(calc.subtract(5, 0),5)


    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(10, 0), 0)


    def divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, -2), -5)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(calc.divide(10, 0))
        self.assertEqual(calc.divide(0, 10))
        self.assertEqual(calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(calc.divide(1.5, 0.5), 3.0)


if __name == "__main__":
    unittest.main()

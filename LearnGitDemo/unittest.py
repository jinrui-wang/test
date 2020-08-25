from unittest import TestCase


class TestCalculator(unittest,TestCase):
    def test_add(self):
        c=Calculator(3,5)
        result=c.add
        self.assertEqual(result,8)

import unittest

from src.utils import *


class TestCalcPercentHeight(unittest.TestCase):
    def test_returns_120(self):
        self.assertEqual(calc_percent_length(25, 480), 120)

    def test_returns_240(self):
        self.assertEqual(calc_percent_length(50, 480), 240)


if __name__ == '__main__':
    unittest.main()

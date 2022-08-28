import unittest

from SumOfThe import SumOfThe

class TestSumOfThe(unittest.TestCase):
    def test_sum_of_the(self):
        result = SumOfThe(5, [5, -25, 10, -35, -45])
        self.assertEqual(result, -45)

if __name__ == "__main__":
    unittest.main()

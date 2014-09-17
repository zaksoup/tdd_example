from factors import *
import unittest

class TestRecursionMuscles(unittest.TestCase):

  def test_prime_factors(self):
    self.assertEqual(factors(2), [2])
    self.assertEqual(factors(3), [3])
    self.assertEqual(factors(4), [2, 2])
    self.assertEqual(factors(51), [3, 17])

if __name__ == '__main__':
    unittest.main()
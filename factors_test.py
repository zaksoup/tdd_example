from factors import *
import unittest

class TestRecursionMuscles(unittest.TestCase):

  def test_prime_factors(self):
    self.assertEqual(factors(2), 2)

if __name__ == '__main__':
    unittest.main()
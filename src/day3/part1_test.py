import unittest

from part1 import calculate_result

class TestDay3Part1(unittest.TestCase):
    def test_sample(self):
        input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(calculate_result(input), 161)

if __name__ == '__main__':
    unittest.main()

import unittest

from part1 import calculate_result

class TestDay2Part1(unittest.TestCase):
    def test_sample(self):
        input = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"
        ]
        self.assertEqual(calculate_result(input), 2)

if __name__ == '__main__':
    unittest.main()

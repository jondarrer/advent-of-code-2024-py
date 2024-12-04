import unittest

from part1 import calculate_result

class TestDay4Part1(unittest.TestCase):
    def test_sample(self):
        input = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
        self.assertEqual(calculate_result(input), 18)

if __name__ == '__main__':
    unittest.main()

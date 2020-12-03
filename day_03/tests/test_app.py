import unittest
from day_03.app import count_trees, multiply_count_trees_for_multiple_direction_options


class AppTestCase(unittest.TestCase):
    def test_count_trees_ok(self):
        path = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#',
        ]

        total_trees_option_one = count_trees(path, 1, 1)
        total_trees_option_two = count_trees(path, 3, 1)
        total_trees_option_three = count_trees(path, 5, 1)
        total_trees_option_four = count_trees(path, 7, 1)
        total_trees_option_five = count_trees(path, 1, 2)

        self.assertEquals(2, total_trees_option_one)
        self.assertEquals(7, total_trees_option_two)
        self.assertEquals(3, total_trees_option_three)
        self.assertEquals(4, total_trees_option_four)
        self.assertEquals(2, total_trees_option_five)

    def test_count_trees_for_multiple_direction_options(self):
        path = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#',
        ]

        result = multiply_count_trees_for_multiple_direction_options(path, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

        self.assertEquals(336, result)


if __name__ == '__main__':
    unittest.main()

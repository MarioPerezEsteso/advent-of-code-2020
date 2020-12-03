import unittest
from day_03.app import count_trees


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

        total_trees = count_trees(path)

        self.assertEquals(7, total_trees)


if __name__ == '__main__':
    unittest.main()

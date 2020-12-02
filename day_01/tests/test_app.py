import unittest

from day_01.app import find_two_entries_that_sum_2020, multiply, find_three_entries_that_sum_2020


class AppTestCase(unittest.TestCase):
    def test_find_two_entries_that_sum_2020_ok(self):
        entries = [
            979,
            366,
            675,
            1456,
            1721,
            299,
        ]

        number_one, number_two = find_two_entries_that_sum_2020(entries)

        self.assertEqual(number_one, 1721)
        self.assertEqual(number_two, 299)

    def test_find_two_entries_that_sum_2020_with_one_number_throws_error(self):
        entries = [10]

        with self.assertRaises(Exception):
            find_two_entries_that_sum_2020(entries)

    def test_find_two_entries_that_sum_2020_with_numbers_dont_sum_2020_throws_error(self):
        entries = [1010, 1000]

        with self.assertRaises(Exception):
            find_two_entries_that_sum_2020(entries)

    def test_find_three_entries_that_sum_2020(self):
        entries = [
            1456,
            1721,
            979,
            366,
            299,
            675,
        ]

        number_one, number_two, number_three = find_three_entries_that_sum_2020(entries)

        self.assertEqual(number_one, 979)
        self.assertEqual(number_two, 366)
        self.assertEqual(number_three, 675)

    def test_find_three_entries_that_sum_2020_with_two_numbers_throws_error(self):
        entries = [10, 10]

        with self.assertRaises(Exception):
            find_three_entries_that_sum_2020(entries)

    def test_find_three_entries_that_sum_2020_with_numbers_dont_sum_2020_throws_error(self):
        entries = [1010, 1000, 9]

        with self.assertRaises(Exception):
            find_three_entries_that_sum_2020(entries)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3, 5), 30)

    def test_multiplication_with_only_one_number_throws_error(self):
        with self.assertRaises(Exception):
            multiply(10)

    def test_multiplication_without_numbers_throws_error(self):
        with self.assertRaises(Exception):
            multiply()


if __name__ == '__main__':
    unittest.main()

import unittest

from day_02.app import count_valid_passwords, is_valid_password, format_input_data, format_input_data_for_new_policy, \
    is_valid_password_for_new_policy, count_valid_passwords_for_new_policy


class AppTestCase(unittest.TestCase):
    def test_format_input_ok(self):
        pass

    def test_count_valid_passwords_ok(self):
        passwords = [
            {
                'min_char_appearances': 1,
                'max_char_appearances': 3,
                'mandatory_char': 'a',
                'password': 'abcde'
            },
            {
                'min_char_appearances': 1,
                'max_char_appearances': 3,
                'mandatory_char': 'b',
                'password': 'cdefg'
            },
            {
                'min_char_appearances': 2,
                'max_char_appearances': 9,
                'mandatory_char': 'c',
                'password': 'ccccccccc'
            }
        ]

        number_valid_passwords = count_valid_passwords(passwords=passwords)

        self.assertEqual(number_valid_passwords, 2)

    def test_count_valid_passwords_with_empty_list_returns_zero(self):
        passwords = []

        number_valid_passwords = count_valid_passwords(passwords=passwords)

        self.assertEqual(number_valid_passwords, 0)

    def test_is_valid_password_ok(self):
        password_data = {
            'min_char_appearances': 1,
            'max_char_appearances': 3,
            'mandatory_char': 'a',
            'password': 'abcde'
        }

        is_valid = is_valid_password(password_data=password_data)

        self.assertTrue(is_valid)

    def test_is_valid_password_returns_false_when_char_appears_less_times_than_min(self):
        password_data = {
            'min_char_appearances': 1,
            'max_char_appearances': 3,
            'mandatory_char': 'z',
            'password': 'abcde'
        }

        is_valid = is_valid_password(password_data=password_data)

        self.assertFalse(is_valid)

    def test_is_valid_password_returns_false_when_char_appears_more_times_than_max(self):
        password_data = {
            'min_char_appearances': 1,
            'max_char_appearances': 3,
            'mandatory_char': 'z',
            'password': 'abczzzz'
        }

        is_valid = is_valid_password(password_data=password_data)

        self.assertFalse(is_valid)

    def test_is_valid_password_returns_true_when_char_appears_same_time_min_and_max(self):
        password_data = {
            'min_char_appearances': 3,
            'max_char_appearances': 3,
            'mandatory_char': 'z',
            'password': 'abczzz'
        }

        is_valid = is_valid_password(password_data=password_data)

        self.assertTrue(is_valid)

    def test_format_input_data(self):
        data = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc',
        ]

        result = format_input_data(data)

        expected_result = [
            {
                'min_char_appearances': 1,
                'max_char_appearances': 3,
                'mandatory_char': 'a',
                'password': 'abcde'
            },
            {
                'min_char_appearances': 1,
                'max_char_appearances': 3,
                'mandatory_char': 'b',
                'password': 'cdefg'
            },
            {
                'min_char_appearances': 2,
                'max_char_appearances': 9,
                'mandatory_char': 'c',
                'password': 'ccccccccc'
            }
        ]

        self.assertEqual(result, expected_result)

    def test_format_input_data_for_new_policy(self):
        data = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc',
        ]

        result = format_input_data_for_new_policy(data)

        expected_result = [
            {
                'position_one': 1,
                'position_two': 3,
                'mandatory_char': 'a',
                'password': 'abcde'
            },
            {
                'position_one': 1,
                'position_two': 3,
                'mandatory_char': 'b',
                'password': 'cdefg'
            },
            {
                'position_one': 2,
                'position_two': 9,
                'mandatory_char': 'c',
                'password': 'ccccccccc'
            }
        ]

        self.assertEqual(result, expected_result)

    def test_is_valid_password_for_new_policy_when_char_appears_in_position_one_ok(self):
        data = {
            'position_one': 1,
            'position_two': 3,
            'mandatory_char': 'a',
            'password': 'abcde'
        }

        result = is_valid_password_for_new_policy(data)

        self.assertTrue(result)

    def test_is_valid_password_for_new_policy_when_char_appears_in_position_two_ok(self):
        data = {
            'position_one': 2,
            'position_two': 9,
            'mandatory_char': 'c',
            'password': 'abbbcccccccccc'
        }

        result = is_valid_password_for_new_policy(data)

        self.assertTrue(result)

    def test_is_valid_password_for_new_policy_when_char_appears_in_both_positions_false(self):
        data = {
            'position_one': 1,
            'position_two': 2,
            'mandatory_char': 'c',
            'password': 'cc'
        }

        result = is_valid_password_for_new_policy(data)

        self.assertFalse(result)

    def test_count_valid_passwords_for_new_policy_ok(self):
        passwords = [
            {
                'position_one': 1,
                'position_two': 3,
                'mandatory_char': 'a',
                'password': 'abcde'
            },
            {
                'position_one': 1,
                'position_two': 3,
                'mandatory_char': 'b',
                'password': 'cdefg'
            },
            {
                'position_one': 2,
                'position_two': 9,
                'mandatory_char': 'c',
                'password': 'ccccccccc'
            }
        ]

        number_valid_passwords = count_valid_passwords_for_new_policy(passwords=passwords)

        self.assertEqual(number_valid_passwords, 1)


if __name__ == '__main__':
    unittest.main()

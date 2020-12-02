import csv
from typing import List, Tuple


def find_two_entries_that_sum_2020(entries: List) -> Tuple[int, int]:
    if len(entries) < 2:
        raise Exception('Not enough entries')

    for left_index in range(len(entries) - 1):
        for right_index in range(left_index + 1, len(entries)):
            if entries[left_index] + entries[right_index] == 2020:
                return entries[left_index], entries[right_index]

    raise Exception('No pair of numbers that sum 2020 could be found')


def find_three_entries_that_sum_2020(entries: List) -> Tuple[int, int, int]:
    if len(entries) < 3:
        raise Exception('Not enough entries')

    for left_index in range(len(entries) - 2):
        for middle_index in range(left_index + 1, len(entries) - 1):
            for right_index in range(middle_index + 1, len(entries)):
                if entries[left_index] + entries[middle_index] + entries[right_index] == 2020:
                    return entries[left_index], entries[middle_index], entries[right_index]

    raise Exception('No three of numbers that sum 2020 could be found')


def multiply(*numbers) -> int:
    if len(numbers) < 2:
        raise Exception('Not enough numbers to multiply')

    result = 1
    for number in numbers:
        result = result * number

    return result


def get_csv_input() -> List[int]:
    entries = []
    with open('./resources/entries.csv', newline='') as file:
        for line in file:
            entries.append(int(line))

    return entries


if __name__ == '__main__':
    entries = get_csv_input()
    print("Solution to first problem of day 01:")
    number_one, number_two = find_two_entries_that_sum_2020(entries)
    print(multiply(number_one, number_two))

    print("Solution to second problem of day 01:")
    number_one, number_two, number_three = find_three_entries_that_sum_2020(entries)
    print(multiply(number_one, number_two, number_three))

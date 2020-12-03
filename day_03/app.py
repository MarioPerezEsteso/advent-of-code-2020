from typing import List


def count_trees(map_to_airport: List[str]) -> int:
    height = len(map_to_airport)
    total_trees = 0
    current_vertical_position = 0
    current_horizontal_position = 0
    path_width = len(map_to_airport[0])
    while current_vertical_position < height - 1:
        current_vertical_position += 1
        current_horizontal_position += 3
        if current_horizontal_position >= path_width:
            current_horizontal_position = current_horizontal_position - path_width
        if map_to_airport[current_vertical_position][current_horizontal_position] == '#':
            total_trees += 1

    return total_trees


def get_input() -> List[str]:
    lines = []
    with open('./resources/input.txt', newline='') as file:
        for line in file:
            lines.append(line.rstrip())

    return lines


if __name__ == '__main__':
    entries = get_input()
    map_to_airport = get_input()
    print("Solution to first problem of day 03:")
    print(count_trees(map_to_airport))

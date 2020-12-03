from typing import List, Tuple


def count_trees(map_to_airport: List[str], move_positions_right: int, move_positions_down: int) -> int:
    height = len(map_to_airport)
    total_trees = 0
    current_vertical_position = 0
    current_horizontal_position = 0
    path_width = len(map_to_airport[0])
    while current_vertical_position < height - 1:
        current_vertical_position += move_positions_down
        current_horizontal_position += move_positions_right

        if current_horizontal_position >= path_width:
            current_horizontal_position = current_horizontal_position - path_width

        if map_to_airport[current_vertical_position][current_horizontal_position] == '#':
            total_trees += 1

    return total_trees


def multiply_count_trees_for_multiple_direction_options(map_to_airport: List[str], directions: List[Tuple]) -> int:
    multiplication = 1
    for move_position_right, move_position_down in directions:
        multiplication = multiplication * count_trees(map_to_airport, move_position_right, move_position_down)

    return multiplication


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
    print(count_trees(map_to_airport, 3, 1))

    print("Solution to second problem of day 03:")
    print(multiply_count_trees_for_multiple_direction_options(map_to_airport, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))

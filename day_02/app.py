from typing import List, Dict


def count_valid_passwords(passwords: List[Dict]) -> int:
    valid_password_count = 0
    for password_data in passwords:
        if is_valid_password(password_data=password_data):
            valid_password_count += 1

    return valid_password_count


def count_valid_passwords_for_new_policy(passwords: List[Dict]) -> int:
    valid_password_count = 0
    for password_data in passwords:
        if is_valid_password_for_new_policy(password_data=password_data):
            valid_password_count += 1

    return valid_password_count


def is_valid_password(password_data: Dict) -> bool:
    min_char_appearances = password_data['min_char_appearances']
    max_char_appearances = password_data['max_char_appearances']
    mandatory_char = password_data['mandatory_char']
    password = password_data['password']

    appearances = 0
    for char in password:
        if char == mandatory_char:
            appearances += 1
            if appearances > max_char_appearances:
                return False

    return appearances >= min_char_appearances


def is_valid_password_for_new_policy(password_data: Dict) -> bool:
    position_one = password_data['position_one']
    position_two = password_data['position_two']
    mandatory_char = password_data['mandatory_char']
    password = password_data['password']

    appears_in_pos_one = False
    appears_in_pos_two = False

    if mandatory_char == password[position_one - 1]:
        appears_in_pos_one = True

    if mandatory_char == password[position_two - 1]:
        appears_in_pos_two = True

    return (appears_in_pos_one or appears_in_pos_two) and not (appears_in_pos_one and appears_in_pos_two)


def format_input_data(data: List[str]) -> List[Dict]:
    password_data_list = []
    for password_data in data:
        splitted = password_data.split()
        max_and_min = splitted[0].split('-')
        password_data_list.append({
            'min_char_appearances': int(max_and_min[0]),
            'max_char_appearances': int(max_and_min[1]),
            'mandatory_char': splitted[1][:-1],
            'password': splitted[2]
        })

    return password_data_list


def format_input_data_for_new_policy(data: List[str]) -> List[Dict]:
    password_data_list = []
    for password_data in data:
        splitted = password_data.split()
        positions = splitted[0].split('-')
        password_data_list.append({
            'position_one': int(positions[0]),
            'position_two': int(positions[1]),
            'mandatory_char': splitted[1][:-1],
            'password': splitted[2]
        })

    return password_data_list


def get_input() -> List[str]:
    passwords = []
    with open('./resources/input.txt', newline='') as file:
        for line in file:
            passwords.append(line)

    return passwords


if __name__ == '__main__':
    entries = get_input()
    input = get_input()
    print("Solution to first problem of day 02:")
    passwords_data = format_input_data(data=input)
    print(count_valid_passwords(passwords=passwords_data))

    print("Solution to second problem of day 02:")
    passwords_data = format_input_data_for_new_policy(data=input)
    print(count_valid_passwords_for_new_policy(passwords=passwords_data))

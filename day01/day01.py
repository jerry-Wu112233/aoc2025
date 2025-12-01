
STARTING_POS = 50

def parse_input() -> list[int]:
    results = []
    with open("day01/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            value = int(line[1:])

            if direction == "L":
                results.append(-value)
            elif direction == "R":
                results.append(value)
            else:
                raise ValueError(f"Invalid line: {line}")

    return results


def part1() -> int:
    current_pos = STARTING_POS
    occurrence_of_zero = 0
    for command in parse_input():
        current_pos = (current_pos + command) % 100
        if current_pos == 0:
            occurrence_of_zero += 1
    return occurrence_of_zero


def part2() -> int:
    current_pos = STARTING_POS
    occurrence_of_zero = 0
    for command in parse_input():
        magnitude = abs(command)
        while magnitude > 0:
            if command < 0:
                current_pos -= 1
            else:
                current_pos += 1
            current_pos %= 100
            if current_pos == 0:
                occurrence_of_zero += 1
            magnitude -= 1
    return occurrence_of_zero

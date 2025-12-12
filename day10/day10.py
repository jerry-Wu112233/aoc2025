import ast
from collections import deque
from dataclasses import dataclass
from scipy.optimize import milp, LinearConstraint, Bounds


@dataclass(frozen=True)
class MachineInfo:
    desired_light_state: str
    buttons: list[tuple[int]]
    electric_signal: tuple[int]


@dataclass(frozen=True)
class Lights:
    state: str
    press_count: tuple[int]


def press(light: Lights, buttons: tuple[int]) -> Lights:
    new_state = ""
    new_press_count = [c for c in light.press_count]

    for i in range(len(light.state)):
        if i not in buttons:
            new_state += light.state[i]
            continue
        if light.state[i] == "#":
            new_state += "."
        else:
            new_state += "#"
        new_press_count[i] += 1

    return Lights(new_state, tuple(new_press_count))


def parse_input():
    with open("day10/input.txt") as f:
        machine_info = []
        for line in f.readlines():
            light_state_raw, *buttons_raw, electric_signal_raw = line.split()

            light_state = light_state_raw[1:-1]
            buttons = [ast.literal_eval(button_raw) for button_raw in buttons_raw]
            for i, button_state in enumerate(buttons):
                if isinstance(button_state, int):
                    buttons[i] = (button_state,)

            electric_sig = tuple(map(int, electric_signal_raw.strip("{}").split(",")))
            machine_info.append(MachineInfo(light_state, buttons, electric_sig))
        return machine_info


def part1() -> int:
    machine_info_list = parse_input()
    return sum(find_least_moves_to_desired_state(machine_info) for machine_info in machine_info_list)


def part2() -> int:
    machine_info_list = parse_input()
    return sum(find_min_moves_for_joltage(machine_info) for machine_info in machine_info_list)


def find_min_moves_for_joltage(machine_info: MachineInfo) -> int:
    n_dim = len(machine_info.desired_light_state)
    A_eq_coefficients = [[0 for _ in range(len(machine_info.buttons))] for _ in range(n_dim)]
    for i, button_state in enumerate(machine_info.buttons):
        for button in button_state:
            A_eq_coefficients[button][i] = 1
    objective_coefficients = [1 for _ in range(len(machine_info.buttons))]

    constraints = LinearConstraint(A_eq_coefficients, machine_info.electric_signal, machine_info.electric_signal)
    integrality = [1 for _ in range(len(machine_info.buttons))]
    optimization_res = milp(
        c=objective_coefficients,
        integrality=integrality,
        constraints=constraints,
    )
    return round(optimization_res.fun)


def find_least_moves_to_desired_state(machine_info: MachineInfo) -> int:
    starting_state = "." * len(machine_info.desired_light_state)
    dawn = Lights(starting_state, tuple(0 for _ in range(len(starting_state))))
    queue = deque([(dawn, 0)])
    visited = set()
    while queue:
        light, moves = queue.popleft()
        if light.state == machine_info.desired_light_state:
            return moves
        if light in visited:
            continue
        visited.add(light)
        for button_set in machine_info.buttons:
            queue.append((press(light, button_set), moves + 1))

    return -1

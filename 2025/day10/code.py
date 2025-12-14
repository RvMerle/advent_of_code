from itertools import combinations
from pathlib import Path

import pulp


def part1_single_line(line: str) -> int:
    input = line.split(" ")

    goal = [c == "#" for c in input[0][1:-1]]
    buttons = [[int(i) for i in button[1:-1].split(",")] for button in input[1:-1]]
    joltage = [int(i) for i in input[-1][1:-1].split(",")]

    for r in range(len(buttons)):
        for combination in combinations(buttons, r):
            current = [False] * len(goal)
            for button in combination:
                for i in button:
                    current[i] = not current[i]
                if current == goal:
                    return r
    raise RuntimeError


def part1(lines: list[str]) -> int:
    return sum(part1_single_line(line) for line in lines)


def part2_single_line(line: str) -> int:
    input = line.split(" ")

    goal = [c == "#" for c in input[0][1:-1]]
    buttons = [[int(i) for i in button[1:-1].split(",")] for button in input[1:-1]]
    joltages = [int(i) for i in input[-1][1:-1].split(",")]

    prob = pulp.LpProblem("joltage_problem", pulp.LpMinimize)
    x = [
        pulp.LpVariable(f"button_{i}", lowBound=0, cat=pulp.LpInteger)
        for i in range(len(buttons))
    ]

    # Minimize number of button presses
    prob += sum(x)

    # s.t. each joltage requirement is met
    for i, joltage in enumerate(joltages):
        prob += sum(x_i for x_i, button in zip(x, buttons) if i in button) == joltage

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if prob.status != pulp.LpStatusOptimal:
        msg = f"Unable to solve this problem, status is {pulp.LpStatus[prob.status]}"
        raise RuntimeError(msg)

    return sum(int(v.varValue) for v in prob.variables() if v.varValue is not None)


def part2(lines: list[str]) -> int:
    return sum(part2_single_line(line) for line in lines)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

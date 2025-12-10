from itertools import combinations
from pathlib import Path


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


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))

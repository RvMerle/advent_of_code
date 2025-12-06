from math import prod
from pathlib import Path


def part1(lines: list[str]) -> list[int]:
    vals = []
    res = []
    for row in lines[:-1]:
        vals.append([val for val in row.strip().split(" ") if val])

    for i, operator in enumerate(
        operator for operator in lines[-1].strip().split(" ") if operator
    ):
        if operator == "+":
            res.append(sum(int(val[i]) for val in vals))
        else:
            res.append(prod(int(val[i]) for val in vals))
    return res


def part2(lines: list[str]) -> list[int]:
    res = []

    operator = lines[-1][0]
    nums = []
    for i in range(len(lines[0])):
        num = "".join(line[i] for line in lines[:-1]).strip()

        if num:
            nums.append(int(num))
        if (not num) or (i == len(lines[0]) - 1):
            if operator == "+":
                res.append(sum(nums))
            else:
                res.append(prod(nums))
            nums.clear()

            if i != len(lines[0]) - 1:
                operator = lines[-1][i + 1]
    return res


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", sum(part1(lines)))
    print("Part 2:", sum(part2(lines)))

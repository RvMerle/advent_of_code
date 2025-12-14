from pathlib import Path
from typing import Sequence


def part1(lines: Sequence[str]) -> int:
    fit = 0

    for line in lines[30:]:
        size, pieces = line.split(": ")

        x, y = size.split("x")
        num_pieces = sum(int(piece) for piece in pieces.split(" "))

        if (int(x) // 3) * (int(y) // 3) >= num_pieces:
            fit += 1

    return fit


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))

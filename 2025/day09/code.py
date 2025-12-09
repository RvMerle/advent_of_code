from pathlib import Path


def part1(lines: list[str]) -> int:
    max_area = 0
    for i, line1 in enumerate(lines[:-1]):
        x1, y1 = line1.split(",")
        for line2 in lines[i + 1 :]:
            x2, y2 = line2.split(",")

            area = abs(int(x1) - int(x2) + 1) * abs(int(y1) - int(y2) + 1)
            max_area = max(area, max_area)

    return max_area


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))

from pathlib import Path


def part1(lines: list[str]) -> int:
    dial_position = 50
    hits = 0

    for line in lines:
        direction, distance = line[:1], int(line[1:])
        if direction == "R":
            dial_position += distance
        else:
            dial_position -= distance

        dial_position %= 100
        if dial_position == 0:
            hits += 1

    return hits


def part2(lines: list[str]) -> int:
    dial_position = 50
    hits = 0
    for line in lines:
        direction, distance = line[:1], int(line[1:])
        if direction == "R":
            dial_position += distance
        else:
            dial_position -= distance

        hits += abs(dial_position) // 100
        if dial_position <= 0 and dial_position + distance != 0:
            # Went from positive to negative, and previous position did not end on a 0
            hits += 1
        dial_position %= 100
    return hits


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

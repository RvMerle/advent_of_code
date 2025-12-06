from pathlib import Path


def part1(ranges: list[str], items: list[str]) -> int:
    res = 0
    for item in items:
        for r in ranges:
            start, end = r.split("-")
            if int(start) <= int(item) <= int(end):
                res += 1
                break
    return res


def part2(ranges: list[str]) -> int:
    combined_ranges: list[tuple[int, int]] = []

    for r in ranges:
        start, end = r.split("-")
        combined_ranges.append((int(start), int(end)))

    combined_ranges.sort()

    i = 0
    while i < len(combined_ranges) - 1:
        if combined_ranges[i][1] >= combined_ranges[i + 1][0]:
            combined_ranges[i] = (
                combined_ranges[i][0],
                max(combined_ranges[i][1], combined_ranges[i + 1][1]),
            )
            combined_ranges.pop(i + 1)
        else:
            i += 1

    return sum(r[1] - r[0] + 1 for r in combined_ranges)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        ranges = []

        while True:
            line = f.readline().strip("\n")
            if line == "":
                break
            ranges.append(line)

        items = f.read().splitlines()

    print("Part 1:", part1(ranges, items))
    print("Part 2:", part2(ranges))

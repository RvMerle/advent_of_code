from pathlib import Path


def part1(line: str) -> int:
    parts = line.split(",")
    ids = []

    for part in parts:
        start, end = part.split("-")

        for i in range(int(start), int(end) + 1):
            s = str(i)
            if len(s) % 2:
                # ID needs to have even length to repeat itself
                continue

            # Check if first half equals second half
            mid = len(s) // 2
            if s[:mid] == s[mid:]:
                ids.append(i)

    return sum(ids)


def part2(line: str) -> int:
    parts = line.split(",")
    ids = []

    for part in parts:
        start, end = part.split("-")

        for i in range(int(start), int(end) + 1):
            s = str(i)
            for part_length in range(1, len(s) // 2 + 1):
                # Try all lengths of sequences (1, 2, etc.)

                if len(s) % part_length:
                    # Original ID is not divisible in equal parts of length part_length
                    continue

                # Check if each part is equal
                parts = [
                    s[j * part_length : (j + 1) * part_length]
                    for j in range(len(s) // part_length)
                ]
                if all(part == parts[0] for part in parts):
                    ids.append(i)
                    break

    return sum(ids)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        line = f.readline()

    print("Part 1:", part1(line))
    print("Part 2:", part2(line))

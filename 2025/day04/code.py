from pathlib import Path


def part1(diagram: list[str]) -> tuple[list[str], int]:
    res = []
    count = 0
    for i in range(len(diagram)):
        row = ""
        for j in range(len(diagram[0])):
            if diagram[i][j] == "@" and (
                sum(
                    int(diagram[k][l] == "@")
                    for k in range(max(i - 1, 0), min(i + 2, len(diagram)))
                    for l in range(max(j - 1, 0), min(j + 2, len(diagram[0])))
                )
                <= 4
            ):
                row += "."
                count += 1
            else:
                row += diagram[i][j]
        res.append(row)

    return res, count


def part2(diagram: list[str]) -> int:
    total_count = 0
    prev_diagram = []
    new_diagram = diagram
    while new_diagram != prev_diagram:
        prev_diagram = new_diagram
        new_diagram, count = part1(new_diagram)
        total_count += count
    return total_count


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines)[1])
    print("Part 2:", part2(lines))

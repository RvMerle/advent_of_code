from pathlib import Path


def part1(lines: list[str]) -> int:
    splits = 0
    beams = [lines[0].find("S")]
    for line in lines:
        new_beams = set()
        for beam in beams:
            if line[beam] == ".":
                new_beams.add(beam)
            else:
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                splits += 1
        beams = list(new_beams)
    return splits


def part2(lines: list[str]):
    beams = [(lines[0].find("S"), 1)]

    for line in lines:
        new_beams = []
        for beam in beams:
            if line[beam[0]] == ".":
                new_beams.append(beam)
            else:
                new_beams.append((beam[0] - 1, beam[1]))
                new_beams.append((beam[0] + 1, beam[1]))
        unique_beams = set(beam[0] for beam in new_beams)
        beams = [
            (
                unique_beam,
                sum(beam[1] if beam[0] == unique_beam else 0 for beam in new_beams),
            )
            for unique_beam in unique_beams
        ]
    return sum(beam[1] for beam in beams)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

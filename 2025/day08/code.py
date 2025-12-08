import math
from pathlib import Path


def part1(lines: list[str], n: int = 1000) -> int:
    coordinates = [[int(i) for i in line.split(",")] for line in lines]
    dist = sorted(
        [
            (math.dist(coordinates[i], coordinates[j]), i, j)
            for i in range(len(coordinates) - 1)
            for j in range(i + 1, len(coordinates))
        ]
    )[:n]

    circuits: list[set[int]] = []
    for _, c1, c2 in dist:
        i1 = next((i for i, circuit in enumerate(circuits) if c1 in circuit), None)
        i2 = next((i for i, circuit in enumerate(circuits) if c2 in circuit), None)

        if i1 is not None and i2 is not None:
            if i1 == i2:
                # Both junctions are already in the same circuit
                continue

            # Combine both existing circuits
            circuits[i1].update(circuits.pop(i2))
        elif i1 is not None:
            # Add junction 2 to existing circuit of junction 1
            circuits[i1].add(c2)
        elif i2 is not None:
            # Add junction 1 to existing circuit of junction 2
            circuits[i2].add(c1)
        else:
            # Create new circuit with junctions 1 and 2
            circuits.append({c1, c2})

    circuits.sort(key=lambda circuit: len(circuit), reverse=True)
    return math.prod(len(circuit) for circuit in circuits[:3])


def part2(lines: list[str]) -> int:
    coordinates = [[int(i) for i in line.split(",")] for line in lines]
    dist = sorted(
        [
            (math.dist(coordinates[i], coordinates[j]), i, j)
            for i in range(len(coordinates) - 1)
            for j in range(i + 1, len(coordinates))
        ]
    )

    circuits: list[set[int]] = []
    for _, c1, c2 in dist:
        i1 = next((i for i, circuit in enumerate(circuits) if c1 in circuit), None)
        i2 = next((i for i, circuit in enumerate(circuits) if c2 in circuit), None)

        if i1 is not None and i2 is not None:
            if i1 == i2:
                # Both junctions are already in the same circuit
                continue

            # Combine both existing circuits
            circuits[i1].update(circuits.pop(i2))
        elif i1 is not None:
            # Add junction 2 to existing circuit of junction 1
            circuits[i1].add(c2)
        elif i2 is not None:
            # Add junction 1 to existing circuit of junction 2
            circuits[i2].add(c1)
        else:
            # Create new circuit with junctions 1 and 2
            circuits.append({c1, c2})

        if len(circuits) == 1 and len(circuits[0]) == len(lines):
            return coordinates[c1][0] * coordinates[c2][0]

    return -1


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

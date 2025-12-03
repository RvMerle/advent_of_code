from pathlib import Path


def part1(banks: list[str]) -> list[int]:
    res = []

    for bank in banks:
        first, second = bank[0], bank[1]

        for i in range(len(bank) - 1):
            char, next_char = bank[i], bank[i + 1]
            if char > first:
                first = char
                second = next_char
            elif next_char > second:
                second = next_char

        res.append(int(first + second))

    return res


def part2(banks: list[str]) -> list[int]:
    res = []

    for bank in banks:
        chosen_batteries = []
        for i, battery in enumerate(bank):
            for j, chosen_battery in enumerate(chosen_batteries):
                if len(bank) - i >= 12 - j and battery > chosen_battery:
                    chosen_batteries = chosen_batteries[:j]
                    chosen_batteries.append(battery)
                    break
            else:
                if len(chosen_batteries) < 12:
                    chosen_batteries.append(battery)

        res.append(int("".join(chosen_batteries)))
    return res


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", sum(part1(lines)))
    print("Part 2:", sum(part2(lines)))

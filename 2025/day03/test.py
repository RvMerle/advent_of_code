from .code import part1, part2


def test_part1_sample():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    result = part1(banks)

    assert result == [98, 89, 78, 92]


def test_part2_sample():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    result = part2(banks)

    assert result == [987654321111, 811111111119, 434234234278, 888911112111]

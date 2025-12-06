from .code import part1, part2


def test_part1_sample():
    ranges = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
    ]
    items = [
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
    result = part1(ranges, items)

    assert result == 3


def test_part2_sample():
    ranges = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
    ]
    result = part2(ranges)

    assert result == 14

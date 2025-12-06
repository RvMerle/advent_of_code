from .code import part1, part2


def test_part1_sample():
    lines = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]
    result = part1(lines)

    assert result == [33210, 490, 4243455, 401]


def test_part2_sample():
    lines = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]
    result = part2(lines)

    assert result == [8544, 625, 3253600, 1058]

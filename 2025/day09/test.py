from .code import part1


def test_part1_sample():
    lines = [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3",
    ]
    assert part1(lines) == 50

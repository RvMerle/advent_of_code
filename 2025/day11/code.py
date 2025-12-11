from collections import defaultdict
from pathlib import Path


def _calc_num_paths(paths: dict[str, list[str]], start: str, end: str) -> int:
    num_paths: dict[str, int] = defaultdict(int)
    num_paths[start] = 1

    next_nodes: set[str] = set([start])
    res = 0
    for _ in range(len(paths)):
        new_next_nodes = set()
        new_num_paths = defaultdict(int)
        for node in next_nodes:
            if node not in paths:
                continue
            for destination in paths[node]:
                new_num_paths[destination] += num_paths[node]
                new_next_nodes.add(destination)
        next_nodes = new_next_nodes
        num_paths = new_num_paths
        res += num_paths[end]
        if not next_nodes:
            break
    if next_nodes:
        raise RuntimeError("Found cycles")

    return res


def part1(lines: list[str]) -> int:
    paths: dict[str, list[str]] = {
        line.split(": ")[0]: line.split(": ")[1].split(" ") for line in lines
    }
    return _calc_num_paths(paths, "you", "out")


def part2(lines: list[str]) -> int:
    paths: dict[str, list[str]] = {
        line.split(": ")[0]: line.split(": ")[1].split(" ") for line in lines
    }

    paths_without_dac = paths.copy()
    del paths_without_dac["dac"]
    paths_without_fft = paths.copy()
    del paths_without_fft["fft"]

    print("svr -> fft", _calc_num_paths(paths_without_dac, "svr", "fft"))
    print("fft -> dac", _calc_num_paths(paths, "fft", "dac"))
    print("dac -> out", _calc_num_paths(paths_without_fft, "dac", "out"))

    print("svr -> dac", _calc_num_paths(paths_without_fft, "svr", "dac"))
    print("dac -> fft", _calc_num_paths(paths, "dac", "fft"))
    print("fft -> out", _calc_num_paths(paths_without_dac, "fft", "out"))

    print("svr -> out", _calc_num_paths(paths, "svr", "out"))

    return _calc_num_paths(paths_without_dac, "svr", "fft") * _calc_num_paths(
        paths, "fft", "dac"
    ) * _calc_num_paths(paths_without_fft, "dac", "out") + _calc_num_paths(
        paths_without_fft, "svr", "dac"
    ) * _calc_num_paths(paths, "dac", "fft") * _calc_num_paths(
        paths_without_dac, "fft", "out"
    )


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

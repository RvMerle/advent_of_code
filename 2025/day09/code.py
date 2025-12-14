from pathlib import Path

import matplotlib.pyplot as plt
import shapely
from shapely import plotting


def part1(lines: list[str]) -> int:
    max_area = 0
    for i, line1 in enumerate(lines[:-1]):
        x1, y1 = line1.split(",")
        for line2 in lines[i + 1 :]:
            x2, y2 = line2.split(",")

            area = abs(int(x1) - int(x2) + 1) * abs(int(y1) - int(y2) + 1)
            max_area = max(area, max_area)

    return max_area


def part2(lines: list[str], *, enable_plotting: bool = False) -> int:
    max_area = 0
    exterior = shapely.Polygon(
        [(int(line.split(",")[0]), -int(line.split(",")[1])) for line in lines]
    )

    for i, line1 in enumerate(lines[:-1]):
        x1, y1 = line1.split(",")
        x1, y1 = int(x1), -int(y1)
        for line2 in lines[i + 1 :]:
            x2, y2 = line2.split(",")
            x2, y2 = int(x2), -int(y2)

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area and exterior.contains(
                shapely.box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            ):
                max_area = area

                if enable_plotting:
                    print("New maximum area:", area)
                    plt.plot(*plotting.plot_polygon(exterior)[1].get_data())
                    plt.plot(
                        *plotting.plot_polygon(
                            shapely.box(
                                min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
                            )
                        )[1].get_data()
                    )
                    plt.show()

    return max_area


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt") as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines, enable_plotting=True))

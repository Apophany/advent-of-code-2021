import sys

from util import file_reader


def sonar_sweep(measurements: list[int]):
    prev = sys.maxsize
    count = 0

    for measurement in measurements:
        if measurement > prev:
            count = count + 1
        prev = measurement

    return count


if __name__ == "__main__":
    result = sonar_sweep(file_reader.read("input.txt"))
    print(result)

from util import file_reader
from typing import List

NUM_BITS = 12


def diagnose(inputs: List[str]) -> int:
    bit_counts = [0] * NUM_BITS

    for input in inputs:
        input = input.replace("\n", "")
        for idx, val in enumerate(input):
            if val == '1':
                bit_counts[idx] += 1
            else:
                bit_counts[idx] -= 1

    gamma = 0
    for idx, val in reversed(list(enumerate(bit_counts))):
        if val > 0:
            gamma = gamma | (1 << NUM_BITS - 1 - idx)

    epsilon = ((1 << NUM_BITS) - 1 - gamma)
    return gamma * epsilon


if __name__ == "__main__":
    result = diagnose(file_reader.read("../input.txt"))
    print(result)

from typing import List
from util import file_reader

NUM_BITS = 12


def diagnose(inputs: List[str]) -> int:
    bit_counts = [0] * NUM_BITS

    oxygen_vals = inputs.copy()
    co2_vals = inputs.copy()

    for input in inputs:
        input = input.replace("\n", "")
        for idx, val in enumerate(input):
            if val == '1':
                bit_counts[idx] += 1
            else:
                bit_counts[idx] -= 1

    for bit_idx, bit in enumerate(bit_counts):
        for oxygen_idx, oxygen in enumerate(inputs):
            check_bit = "1" if bit > 0 else "0"
            if not oxygen[bit_idx] == check_bit and len(oxygen_vals) > 1 and oxygen_vals.__contains__(oxygen):
                oxygen_vals.remove(oxygen)

        for co2_idx, co2 in enumerate(inputs):
            check_bit = "0" if bit > 0 else "1"
            if not co2[bit_idx] == check_bit and len(co2_vals) > 1 and co2_vals.__contains__(co2):
                co2_vals.remove(co2)

    return int(oxygen_vals[0].replace("/n", ""), 2) * int(co2_vals[0].replace("/n", ""), 2)


if __name__ == "__main__":
    result = diagnose(file_reader.read("../input.txt"))
    print(result)

from util import file_reader


def sonar_sweep_window(inputs: list[int]) -> int:
    window = []
    count = 0

    for input in inputs:
        window.append(input)

        if len(window) > 4:
            window.pop(0)

        if len(window) == 4:
            win1 = window[0] + window[1] + window[2]
            win2 = window[1] + window[2] + window[3]

            count = count + 1 if win2 > win1 else count

    return count

# Use the fact that the delta between the windows can be computed using the
# difference between the first and last values
def sonar_sweep_window_v2(inputs: list[int]) -> int:
    if len(inputs) < 4:
        return 0

    count = 0
    for idx in range(3, len(inputs)):
        if inputs[idx] > inputs[idx - 3]:
            count += 1

    return count


if __name__ == "__main__":
    result = sonar_sweep_window_v2(file_reader.read_int_file("../input.txt"))
    print(result)

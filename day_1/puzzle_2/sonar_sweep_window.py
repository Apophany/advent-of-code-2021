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


if __name__ == "__main__":
    result = sonar_sweep_window(file_reader.read("../input.txt"))
    print(result)

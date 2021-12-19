from util import file_reader

def dive(inputs: list[str]) -> int:
    x_axis = 0
    y_axis = 0

    for input in inputs:
        parts = input.split()

        if parts[0] == 'forward':
            x_axis += int(parts[1])
        if parts[0] == 'up':
            y_axis -= int(parts[1])
        if parts[0] == 'down':
            y_axis += int(parts[1])

    return x_axis * y_axis

if __name__ == "__main__":
    result = dive(file_reader.read("../input.txt"))
    print(result)
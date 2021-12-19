from util import file_reader

def dive_with_aim(inputs: list[str]) -> int:
    aim = 0
    x_axis = 0
    y_axis = 0

    for input in inputs:
        command, value = input.split()
        value = int(value)

        if command == 'forward':
            x_axis += value
            y_axis += value * aim
        if command == 'up':
            aim -= value
        if command == 'down':
            aim += value

    return x_axis * y_axis

if __name__ == "__main__":
    result = dive_with_aim(file_reader.read("../input.txt"))
    print(result)
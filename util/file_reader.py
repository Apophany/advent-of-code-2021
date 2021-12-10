def read(file_name):
    with open("input.txt") as input_file:
        return [int(i) for i in input_file.readlines()]
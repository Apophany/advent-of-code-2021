def read_int_file(file_name):
    with open(file_name) as input_file:
        return [int(line) for line in input_file.readlines()]


def read(file_name):
    with open(file_name) as input_file:
        return input_file.readlines()

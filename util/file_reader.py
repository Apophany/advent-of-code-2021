def read(file_name):
    with open(file_name) as input_file:
        return [int(i) for i in input_file.readlines()]
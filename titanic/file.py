import os


def write_file(sub_dirname, filename, data_to_file):
    if not os.path.exists(os.path.join("output", sub_dirname)):
        os.makedirs(os.path.join("output", sub_dirname))

    with open(os.path.join("output", sub_dirname, filename), mode="w") as f:
        f.write(data_to_file)

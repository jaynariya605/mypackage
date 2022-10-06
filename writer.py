import sys

class Writer:
    def __init__(self):
        path  = sys.argv[2]
        line = str(input("Write here whatever you want to write in file: "))
        with open(path, "w") as f:
            f.write(line)
        
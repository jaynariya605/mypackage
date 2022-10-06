import sys
import os

class Reader:
    def __init__(self, path):
        if not os.path.exists(path):
            print("No file exists")
        else:
            with open(path, "r") as f:
                for line in f.readlines():
                    print(line)



import sys
import os

class Reader:
    def __init__(self):
        path  = sys.argv[2]
        if not os.path.exists(path):
            print("No file exists")
        else:
            with open(path, "r") as f:
                print(f.readlines())



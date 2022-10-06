from .writer import Writer
from .reader import Reader
import sys

if len(sys.argv) < 3:
    print("Write command as python -m mypackage writer/reader pathtofile ")
    exit()
    
operation, path = sys.argv[1], sys.argv[2]

if operation == "writer":
    line = str(input("Write here whatever you want to write in file: "))
    Writer(path, line)
    exit()

Reader(path)
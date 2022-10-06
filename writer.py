
class Writer:
    def __init__(self,path, line):
        with open(path, "w") as f:
            f.write(line)
        
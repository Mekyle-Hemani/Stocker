import os
def write(path, line):
    with open(path, 'a') as f:
        f.write(line + '\n')
    return

def read(path):
    with open(path, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines
    
def create(path):
    with open(path, "w") as f:
        return
    
def delete(path):
    os.remove(path)
    return
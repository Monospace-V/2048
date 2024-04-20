# operations

import core





def new_val(lines):
    positions = []
    for pos in range(len(lines)):
        if lines[pos][-1] == 0:
            positions.append(pos)
    if positions:
        chosen=random.choice(position)
        lines[chosen][-1] = 2
    return lines

def swipe(line):
    for pos in range(len(line) - 1):
        if line[pos] == line[pos + 1]:
            line[pos:pos+1] = [line[pos] * 2, 0]
    return line

def rebalance(line):
    size = len(line)
    new = []
    for value in line:
        if value: new.append(value)
    for rem in size-len(new):
        new.append(0)
    return new
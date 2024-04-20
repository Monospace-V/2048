# operations

import core
import random

def add_val(lines):
    positions = []
    for pos in range(len(lines)):
        if lines[pos][-1] == 0:
            positions.append(pos)
    if positions:
        chosen=random.choice(positions)
        lines[chosen][-1] = 2
    return lines

def swipe(line, size):
    prev = 0
    while (prev < size):
        line = rebalance(line, size)
        for pos in range(prev, size - 1):
            if line[pos] == line[pos + 1]:
                line[pos:pos+2] = [line[pos] * 2]
                prev = pos + 1
                break
        else: break
    return line

def rebalance(line, size):
    new = []
    for value in line:
        if value: new.append(value)
    for rem in range(size-len(new)):
        new.append(0)
    return new
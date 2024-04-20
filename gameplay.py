# game

from core import *
import game_functions as actions

current = grid(4)

def process(lines, reverse = False):
    for i in range(len(lines)):
        line = lines[i]
        line = actions.swipe(line, current.size)
        line = actions.rebalance(line, current.size)
        lines[i] = line
    lines = actions.add_val(lines)
    return lines
    

def swipe_down():
    columns = current.vertical(reverse = True)
    columns = process(columns)
    rows = invert(columns, current.size)
    rows = rows[::-1]
    return rows

def swipe_up():
    columns = current.vertical()
    columns = process(columns)
    rows = invert(columns, current.size)
    return rows

def swipe_right():
    rows = current.horizontal(reverse = True)
    rows = process(rows)
    for i in range(len(rows)):
        rows[i] = rows[i][::-1]        
    return rows

def swipe_left():
    rows = current.horizontal()
    rows = process(rows)
    return rows
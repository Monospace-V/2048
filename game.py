import gameplay
from core import *
import ui_functions as user_in
import ui_output as user_show

grid = grid(4)

def update(new):
    gameplay.current.update(new)
    gameplay.matrix = new

while True:
    action = user_in.get_string("choice", ["W","A","S","D"])
    if action == False: break
    if action == "W":
        rows = gameplay.swipe_up()
    if action == "A":
        rows = gameplay.swipe_left()
    if action == "S":
        rows = gameplay.swipe_down()
    if action == "D":
        rows = gameplay.swipe_right()
    gameplay.current.update(rows)
    user_show.tabulate(gameplay.current.rows)

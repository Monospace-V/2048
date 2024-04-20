
def get_string(requested, choices = False):
    while True:
        str_shown = "Enter " + requested + " "
        if choices:
            for choice in choices:
                str_shown += choice+"/"
        str_shown += "(Q to quit): "
        value=input(str_shown).upper().strip() # Convert to uppercase regardless; strip.
        if value == "Q":
            return False
        if choices and (value not in choices):
            print("Invalid choice!")
            continue
        break
    return value

def get_int(requested, clamp = False):
    while True:
        value=input("Enter " + requested + ": ")
        try:
            value=int(value)
        except:
            print("Integer value expected! Try again.")
            continue
        if clamp and (not (min(clamp) <= value <= max(clamp))):
            print("Value out of range! Try again.")
            continue
        break
    return value
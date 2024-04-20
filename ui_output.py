
def tabulate(rows, header = False):
    everything = list(rows)
    if type(header) is str: header = [header]
    if header: everything = [header] + everything
    maxi = 0
    for row in everything:
        for pos in range(len(row)):
            current = len(str(row[pos]))
            if current > maxi: maxi = current
        size = len(row)
    line(maxi, size)
    for row in everything:
        for position in range(len(row)):
            detail = str(row[position])
            tabulation = (maxi) - (len(detail)) + 1
            print(detail, end = " "* tabulation)
        line(maxi, size)


def line(maxi, size):
    length = (maxi + 1) * size - (maxi + 1)//2
    print()
    print("_" * length)

def list_out(header, values):
    print(header)
    for value in values:
        print(tab_str + value)
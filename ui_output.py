
tab=8 # length of tab
tab_str=" "*tab
def tabulate(rows, header = False):
    everything = list(rows)
    if type(header) is str: header = [header]
    if header: everything = [header] + everything
    mapping = {}
    for row in everything:
        for pos in range(len(row)):
            current = len(str(row[pos]))
            maxi = mapping.get(pos) or 0
            if current > maxi: mapping[pos] = current
    line(mapping)
    for row in everything:
        for position in range(len(row)):
            detail = str(row[position])
            tabulation = ((mapping[position] // tab) - (len(detail) // tab)) + 1
            print(detail, end = tab_str * tabulation)
        line(mapping)


def line(mapping):
    length = 0
    for pos in mapping: length += mapping[pos]
    length = ((length // tab) + 1) * tab
    print()
    print("_" * length)

def list_out(header, values):
    print(header)
    for value in values:
        print(tab_str + value)
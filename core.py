class grid:
    def __init__(self, size = 4):
        self.size = size
        rows = []
        for row in range(size):
            rows.append([0] * size)
        self.rows = rows
        self.columns = invert(self.rows, self.size)
    def vertical(self, reverse = False):
        out = []
        for column in self.columns:
            if reverse:
                column = column[::-1]
            out.append(column)
        return out
    def horizontal(self, reverse = False):
        out = []
        for row in self.rows:
            if reverse:
                row = row[::-1]
            out.append(row)
        return out
    def update(self,rows):
        self.rows = rows
        self.columns = invert(rows, self.size)

def invert(lines, size = None):
    if not size:
        size = len(lines)
    sideways = []
    for col_pos in range(size):
        alt = []
        for line in lines:
            alt.append(line[col_pos])
        sideways.append(alt)
    return sideways

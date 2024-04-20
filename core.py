class grid:
    def init(__self__, size = 4):
        __self__.size = size
        rows = []
        for row in range(size):
            rows.append([0] * size)
        __self__.rows = rows
        columns = []
        for col_pos in range(size):
            column = []
            for row in __self__.rows:
                column.append(row[col_pos])
            columns.append(column)
        __self__.columns = columns

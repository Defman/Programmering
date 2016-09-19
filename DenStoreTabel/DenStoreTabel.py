from math import log10 as log


class Table(object):
    def __init__(self, x, y, xs=1, ys=1):
        self.x = x
        self.y = y
        self.xs = xs
        self.ys = ys

    def __str__(self):
        large = int(log(self.x * self.y)) + 1
        result = "{1:>{0}} ".format(large, 1)
        for x in range(self.xs, self.x + 1):
            result += "{1:>{0}} ".format(large, x)
        result += "\n"
        for y in range(self.ys, self.y + 1):
            result += "{1:>{0}} ".format(large, y)
            for x in range(self.xs, self.x + 1):
                result += "{1:>{0}} ".format(large, x * y)
            result += "\n"
        return result


class PartitionTable(object):
    def __init__(self, x, y, px=-1, py=-1):
        px = px if px > 0 else x
        py = py if py > 0 else y
        self.tables = []
        self.px = px
        self.py = py
        for j in range(1, y + 1, self.py):
            for i in range(1, x + 1, self.px):
                self.tables.append(Table(i+px, j+py, i, j))

    def __str__(self):
        return "\n\n".join(map(str, self.tables))
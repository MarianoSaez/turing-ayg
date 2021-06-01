from tabulate import tabulate


class Table:
    def __init__(self, header, rows=list()):
        self.header = header
        self.rows = rows

    def __str__(self):
        return tabulate(self.rows, headers=self.header, tablefmt="fancy_grid")
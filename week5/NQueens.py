from problem import Problem


class NQueens(Problem):

    def __init__(self, N):
        super().__init__(tuple([-1]*N))
        self.N = N

    def actions(self, state):

        if state[-1] != -1:
            return []
        col = state.index(-1)
        return [row for row in range(self.N)
                if not self.conflicted(state, row, col)]

    def result(self, state, row):

        col = state.index(-1)  # az az oszlop ahol lehet még királynőt rakni
        new = list(state[:])  # lemásoljuk az oszlopot
        new[col] = row  # beállítjuk a királyőt
        return tuple(new)

    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        return (
            row1 == row2 or
            col1 == col2 or
            col1 - row1 == col2 - row2 or
            col1 + row1 == col2 + row2
        )

    def goal_test(self, state):
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col) for col in range(len(state)))

    def h(self, node):
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):

                    pass

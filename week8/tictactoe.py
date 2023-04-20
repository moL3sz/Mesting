from game import Game


from collections import namedtuple

GameState = namedtuple("GameState", "to_move, utility, board, moves")


class TicTacToe(Game):

    def __init__(self, h=3, w=3, k=3) -> None:
        self.h = h
        self.w = w
        self.k = k

        moves = [(x, y) for x in range(1, h+1) for y in range(1, w+1)]

        # Kezdő állapot
        self.initial = GameState(to_move="X", utility=0, board={}, moves=moves)

    def actions(self, state):
        return state.moves

    def result(self, state, move):

        if move not in state.moves:
            return state  # Illegáláis lépés

        board = state.board.copy()
        board[move] = state.to_move

        # frissitjük a lépéseket,
        moves = list(state.moves)
        moves.remove(move)

        return GameState(to_move="O" if state.to_move == "X" else "X",
                         utility=self.compute_utility(
                             board, move, state.to_move),
                         moves=moves, board=board)

    def utility(self, state, player):

        return state.utility if player == "X" else -state.utility

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):

        board = state.board

        for x in range(1, self.h+1):
            for y in range(1, self.w+1):
                print(board.get((x, y), "."), end=' ')
            print()

    def compute_utility(self, board, move, player):

        if (self.k_in_row(board, move, player, (0, 1)) or
            self.k_in_row(board, move, player, (1, 0)) or
            self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == "X" else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):

        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0
        while board.get((x, y)) == player:
            n += 1
            x, y = x+delta_x, y+delta_y
        x, y = move

        while board.get((x, y)) == player:
            n += 1
            x, y = x-delta_x, y-delta_y
        n -= 1

        return n >= self.k

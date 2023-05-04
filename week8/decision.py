import numpy as np
from game import Game


def minmax(state, game: Game):
    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -np.inf
        for a in game.actions(state):
             v = max(v, min_value(game.result(state, a)))  # type: ignore

        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = +np.inf
        for a in game.actions(state):
             v = min(v, max_value(game.result(state, a)))  # type: ignore

        return v
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))


def alfa_beta_search(state, game:Game):


    
    player = game.to_move(state)

    def max_value(state, alfa, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -np.inf
        for a in game.actions(state):
             # type: ignore
             v = max(v, min_value(game.result(state, a), alfa, beta))
             # TODO
             if v >= beta:
                 return v
             alfa = max(alfa, v)

        return v

    def min_value(state, alfa, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = +np.inf
        for a in game.actions(state):
            # type: ignore
            v = min(v, max_value(game.result(state, a), alfa, beta))
            # TODO
            if v <= alfa:
                 return v
            beta = min(beta,v)
        return v
    

    best_score = -np.inf
    beta = np.inf
    best_action = None

    for a in game.actions(state):
        v = min_value(game.result(state),best_score,beta)
        if v > best_score:
            best_score = v
            best_action = a

    return best_action
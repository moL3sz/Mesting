import numpy as np



from node import Node
from problem import Problem


def trial_error(problem: Problem):


    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            print("[+] Got it")
            return state


        # lehetésges megoldások
        successor = state.expand(problem)
        if len(successor) == 0:
            return "[-] Unsolvable!"
        state = successor[np.random.randint(0, len(successor))]
        #print(state)

def hill_climbin_for_cup3(problem: Problem,heuristic):


    state = Node(problem.initial)

    while True:
        if problem.goal_test(state.state):
            print("[+] Got it")
            return state


        # lehetésges megoldások
        successor = state.expand(problem)
       
        test_successor = []
        for s_test in successor:
            if heuristic(state.state,) >= heuristic(s_test.state):
                test_successor.append(s_test)

        if len(test_successor) == 0:
            return " [-] Unsolvable"
        state = test_successor[np.random.randint(0, len(test_successor))]
        #print(state)

def heuristic(State):
    if State == (4,0,1) or State == (4,1,0):
        return 0
    c = 0
    for s in State:
        if s == 0:
            c+=1
    return c
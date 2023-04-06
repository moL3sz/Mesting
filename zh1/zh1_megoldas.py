import random

from problem import *
from node import *
# szélességi keresés
def breath_first_search(problem: Problem):
    from collections import deque
    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            #megvan a cél!
            print("[+] Got it!")
            return node
        

        frontier.extend(node.expand(problem))

class Digits(Problem):

    def __init__(self, initial, goal=None):
        self.wrong_numbers = [(6,6,6),(6,6,7)]
        self.s4 = 0

        # Complete the implementation of initial function by calling
        # the parent constructor and initialize the initial state and set of goal states
        # Write your code below this line!
        super().__init__(initial,goal)
        # Write your code above this line! Delete the 'pass' keyword!
        

    def actions(self, state):
        s1, s2, s3 = state
        acts = []

        # Complete the remaining part of the action function
        # Write your code below this line!
        
        for i in range(len(state)):
            next_state_plus = state.copy()
            next_state_plus[i] += 1
            
            next_state_minus = state.copy()
            next_state_minus[i] -= 1
            
            if next_state_minus[i] >= 0 and self.s4 != i+1 and tuple(next_state_minus) not in self.wrong_numbers:
                acts.append(f"s{i+1}_minus")
            if next_state_plus[i] <= 9 and self.s4 != i+1 and tuple(next_state_plus) not in self.wrong_numbers:
                acts.append(f"s{i+1}_plus")

        # Write your code above this line!
        return acts

    def result(self, state, action):         
        # Complete the implementation of result function
        # Write your code below this line!
        newstate = state.copy()
        i,e = int(action.split("_")[0][1:]), 1 if action.split("_")[1] == "plus" else -1
        self.s4 = i
        newstate[i-1] += e
        return newstate
        # Write your code above this line!


if __name__ == '__main__':
    
    d = Digits([5,7,6],[[7,7,7]])
    
    goal = breath_first_search(d)
    if goal:
        print(goal.path())
    pass
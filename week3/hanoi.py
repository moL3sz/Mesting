from problem import Problem
from collections import namedtuple
State=namedtuple("State", ["disk","char"])

class Hanoi(Problem):
    def __init__(self, n):
        self.size = n
        super().__init__("1" * n, "3" * n)

    def actions(self, state):
        
        # state: 211
        # maga az érték az az hogy melyik rúdon van, az meg hogy hanyadik érték az az hogy mekkora a korong:
        # Itt most a legkisebb korong ( 0-ás index ) az a 2. oszlopon van.
        # A közepes korong és a legnagyobb az első oszlopon van.
        
        
        acts = []
        f1 = state.find("1")
        f2 = state.find("2")
        f3 = state.find("3")
        print(f"Current state: {state}")
        
        
        # Ha találunk olyat ami az első oszlopon van és ez kisebb mint a 2. oszlopon lévő,
        # ergo kisebb a korong mint a 2. oszlopon lévő vagy a 2. oszlopon még nincs semmi (f2 == -1), akkor rá tudjuk pakolni
        if -1 < f1 and (f1 < f2 or f2 == -1):
            # Átrakjuk azt az a vizsgált elemet a 2. oszlopra (f2)
            acts.append(State(f1, "2"))

        # Tudunk áttenni a 3. oszlopra az 1. oszlopról.
        if -1 < f1 and (f1 < f3 or f3 == -1):
            acts.append(State(f1, "3"))

        if -1 < f2 and (f2 < f1 or f1 == -1):
            acts.append(State(f2, "1"))

        if -1 < f2 and (f2 < f3 or f3 == -1):
            acts.append(State(f2, "3"))

        if -1 < f3 and (f3 < f1 or f1 == -1):
            acts.append(State(f3, "1"))

        if -1 < f3 and (f3 < f2 or f2 == -1):
            acts.append(State(f3, "2"))

        return acts

    def result(self, state, action):
        # ez a következő állapot
        # disk az hogy hanyadik helyen áll, a char meg hogy hanydik oszlop
        
        disk, char = action
        
        # berakjuk a disket a megfelelő oszlopra
        # mivel a disk reprezentálja a az indexet hogy melyik korong hol van
        return state[0:disk] + char + state[disk + 1:]
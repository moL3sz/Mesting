from problem import Problem





class Cup3(Problem):
    all_acts = ["5-->3", "5-->2", "2-->3", "3-->2", "2-->5", "3-->5"]
    def actions(self, state):
        # Operátorok definiálása
        acts = []
        five,three,two = state
        if five > 0 and three < 3:
            acts.append("5-->3")
        if five > 0 and two < 2:
            acts.append("5-->2")
        if three > 0 and five < 5:
            acts.append("3-->5")
        if two > 0 and five < 5:
            acts.append("2-->5")
        if three > 0 and two < 2:
            acts.append("3-->2")
        if two > 0 and three < 3:
            acts.append("2-->3")
        return acts
    def result(self, state, action):
        five, three,two = state
        d = {5:five, 3:three, 2:two}

        for act in Cup3.all_acts:
            if action == act:
                fr, to = list(map(int, act.split("-->")))
                m = min(d[fr], to - d[to])
                k = list(set(d.keys()) - {fr,to})
                
                dd = sorted( ((fr, d[fr]-m), (k[0], d[k[0]]), (to, d[to]+m)),key=lambda x: -x[0])
                return tuple((p[1] for p in dd))
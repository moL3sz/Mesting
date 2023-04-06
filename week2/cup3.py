from problem import Problem





class Cup3(Problem):
    
    # összes operátor
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
        cup_values_by_label = {5:five, 3:three, 2:two}

        for act in Cup3.all_acts:
            if action == act:
                # kiszedjük az operátorokból hogy melyik korsóbólé melyikbe töltünk.
                from_cup_label, to_cup_label = list(map(int, act.split("-->")))
                
                # m: az az érték amit át tudunk önteni egyik korsóból a másikba.
                pourable_quantity = min(cup_values_by_label[from_cup_label], to_cup_label - cup_values_by_label[to_cup_label])
                
                #A kimaradt korsót nem bántjuk
                left_out_cup = list(set(cup_values_by_label.keys()) - {from_cup_label,to_cup_label})[0]
                
                
                #megkapjuk a következő állapotot, hogy az egyik korsóból átönntjük amennyit tudunk a másikba
                #ezért az egyikből kivonjuk a másikhoz hozzáadjuk azt a mennyiséget
                #a kimaradt korsót meg békén hagyjuk
                #Berendezzük a címkék alapján hogy a "legnagyobb" korsó legyen elől!
                result_state = sorted( ((from_cup_label, cup_values_by_label[from_cup_label]-pourable_quantity),\
                              (left_out_cup, cup_values_by_label[left_out_cup]), \
                              (to_cup_label, cup_values_by_label[to_cup_label]+pourable_quantity)),key=lambda x: -x[0])
                return tuple((label for label, _ in result_state))
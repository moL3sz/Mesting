#!/usr/bin/env python
# coding: utf-8

# # 1. ZH B csoport - Összesen 10 pont - 90 perc áll rendelkezésre a megoldáshoz

# ## Azonosító adatok

# - NÉV:
# - NEPTUN KÓD:

# ## Feladatok

# 1. (2 pont) Adja meg az alábbi probléma jellemzőit, illetve cél és kezdő állapotát:
# - Egy vödörben 12 liter vodkát kell elosztani egyenlő részre két orosz paraszt Igor és Sasha között.
# - Az elosztás után maradjon a vödörben még 4 liter pálinka.
# - Két 7 literes plackjuk van.

# In[ ]:


# Válasz helye. Válaszát szabályos python commentek között adja meg.


# ### Futassa le az alábbi segéd osztályokat

# In[ ]:


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            for s in self.goal:
                if s==state:
                    return True

            return False
        else:
            return state == self.goal
        
    def path_cost(self, c, state1, action, state2):
        return c + 1


# In[ ]:


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(state = next_state, 
                         parent = self, 
                         action = action, 
                         path_cost = problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


# ### Adott a következő állapottér reprezentáció
# 
# #### A farmer, a kecske, a farkas és a káposzta
# - Egy gazda át akar kelni egy folyón, és magával akar vinni egy farkast, egy kecskét és egy káposztát.
# - Van egy csónak, amelybe csak ketten férnek el, ő maga plusz vagy a farkas, a kecske vagy a káposzta. 
# - Ha a farkas és a kecske egyedül vannak egy parton, a farkas megeszi a kecskét. 
# - Ha a kecske és a káposzta egyedül van a parton, a kecske megeszi a káposztát.

# ### Jellemzők
# 
# - A jellemzők legyenek az egyes szereplők az általuk felvehető értékek pedig, hogy átkeltek, avagy nem a folyón.
# - Jelöljük 0-val hogy nem keltek át a folyón és 1-el hogy átkeltek
# - H1 = {0, 1}, farmer
# - H2 = {0, 1}, kecske
# - H3 = {0, 1}, farkas 
# - H4 = {0, 1}, káposzta 

# ### Állapotok halmaza
# 
# - A ⊆ H1xH2xH3xH4
# - Legyen a !-jel a negáció
# - A = {<a1, a2, a3, a4> | <a1, a2, a3, a4> ∈ H1 x H2 x H3 x H4 ∧ [!(a1==1 ∧ a2==0 ∧ a3==0) v !(a1==1 ∧ a2==0 ∧ a4==0)]}

# ### Kezdő állapot:
# 
# - a0 = <0, 0, 0, 0>

# ### Célállapotok:
# 
# - C = <1, 1, 1, 1>

# ### Operátorok:
# 
# - Legyen 1=farmer,2=farkas,3=kecske,4=kápozsta
# - O = {oi} = {oi | i ∈{1,2,3,4}} 
# - Dom(oi)={<a1, a2, a3, a4>  | <a1, a2, a3, a4> ∈ A ∧ (a1=a2 ∧ a3!=a4) v (a1=a4 ∧ a2!=a3) v (a1=a3) v (a2!=a3 ∧ a3!=a4)}
# - oi(<a1, a2, a3, a4> = <b1, b2, b3, b4>)
# - bk, ahol b=1,2,3,4
#     - ak=!ak ∧ a1=!a1, ha k=i ∧ i!=1
#     - a1=!a1, ha k=i ∧ i==1
#     - ak, egyébként

# 2. (3 pont) Készítsen egy osztályt, amely megvalósítja az állapotér reprezentációt a Problem és Node osztályok segítségével. Az állapottér reprezentáció megvalósításához származzon le a Problem osztályból és írja meg annak "állapot átmenet függvényét / operátorok / actions" és "operátor hatás definícióját / result". Ha szükséges bármilyen egyéb program csomag a futtatáshoz annak megadásáról se feledkezzen meg.

# In[ ]:


# Válasz helye. Válaszát futtatható python kóddal adja meg.


# 3. (1 pont) Példányosítsa a reprezentációt a kezdő és cél állapottal majd írassa ki a kezdő sé cél állapotot a "print()" függvény segítségével 

# In[ ]:


# Válasz helye. Válaszát futtatható python kóddal adja meg.


# 4. (1. pont) Írja meg a próba hiba módszert a megoldás megtalálásához. Írjon megjegyzés szabályos python formátumban amiben leírja, hogy pontosan mit csinál az algoritmus. Ha szükséges bármilyen egyéb program csomag a futtatáshoz annak megadásáról se feledkezzen meg.

# In[ ]:


# Válasz helye. Válaszát futtatható python kóddal adja meg.


# 5. (1 pont) Futtasa a próba hiba módszert az elkészített reprezentációra és találja meg a megoldást. 

# In[ ]:


# Válasz helye. Válaszát futtatható python kóddal adja meg.


# 6. (1 pont) Írja meg a mélységi keresést a megoldás megtalálásához. Írjon megjegyzés szabályos python formátumban amiben leírja, hogy pontosan mit csinál az algoritmus. Ha szükséges bármilyen egyéb program csomag a futtatáshoz annak megadásáról se feledkezzen meg.

# In[ ]:


# Válasz helye. Válaszát futtatható python kóddal adja meg.


# 7. (1 pont) Futtasa a mélységi keresést az elkészített reprezentációra és találja meg a megoldást. Ha szükséges bármilyen egyéb program csomag a futtatáshoz annak megadásáról se feledkezzen meg.

# In[ ]:


# Válasz helye. Válaszát futtatható python kóddal adja meg.


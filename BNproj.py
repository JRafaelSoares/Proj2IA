# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""


class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents
        pass
    
    def computeProb(self, evid):

        value = self.prob

        for i in self.parents:
            value = value[evid[i]]

        if len(self.parents) == 0:
            value = self.prob[0]

        return [1-value, value]


#p1 = Node( [[0.001, 0.29],[0.94, 0.95]], [0,1])

#ev = (0, 1, 1, 1, 1)

#print(p1.computeProb(ev))

class BN():
    def __init__(self, gra, prob):
        self.graph = gra
        self.prob = prob
        pass

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        value = 1
        for i in range(0, len(self.graph)):
            value = value*self.prob[i].computeProb(evid)[evid[i]]

        return value

"""
gra = [[], [], [0,1], [2], [2]]

p1 = Node([0.001], gra[0])

p2 = Node([0.002], gra[1])

p3 = Node([[0.001, 0.29],[0.94,0.95]], gra[2])

p4 = Node([0.05, 0.9], gra[3])

p5 = Node([0.01, 0.7], gra[4])

prob = [p1, p2, p3, p4, p5]

bn = BN(gra, prob)

jp = []

for e1 in [0,1]:
    for e2 in [0, 1]:
        for e3 in [0, 1]:
            for e4 in [0, 1]:
                for e5 in [0, 1]:
                    jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))

print("sum joint %.3f (1)" % sum(jp))
"""


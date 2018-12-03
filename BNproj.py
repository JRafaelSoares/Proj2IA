# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np
np.set_printoptions(precision=4, suppress=True)

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

    def computeJointProb(self, evid):
        value = 1
        for i in range(0, len(self.graph)):
            value = value*self.prob[i].computeProb(evid)[evid[i]]

        return value

    def computePostProb(self, evid):
        sum = 0
        alpha = 0
        evid = list(evid)
        for i in range(0, len(evid)):
            if evid[i] == -1:
                pos = i

        evid[pos] = []

        evidences = computeEvidences(evid)

        for i in evidences:
            alpha += self.computeJointProb(i)

        evid[pos] = 1

        evidences = computeEvidences(evid)

        for i in evidences:
            sum += self.computeJointProb(i)

        return sum/alpha

def computeEvidences(evid):
    total_evids = []
    original = list(evid)
    num = -1
    for i in range(0, len(evid)):
        if original[i] == []:
            num = i
            break

    if num == -1:
        return evid

    original[num] = 0

    new_evidence = computeEvidences(tuple(original))

    if isinstance(new_evidence, tuple):
        total_evids.append(new_evidence)
    else:
        for i in new_evidence:
            total_evids.append(i)

    original[num] = 1

    new_evidence = computeEvidences(tuple(original))


    if isinstance(new_evidence, tuple):
        total_evids.append(new_evidence)
    else:
        for i in new_evidence:
            total_evids.append(i)


    return total_evids



gra = [[], [], [0,1], [2], [2]]

p1 = Node(np.array([0.001]), gra[0])

p2 = Node(np.array([0.002]), gra[1])

p3 = Node(np.array([[0.001, 0.29],[0.94,0.95]]), gra[2])

p4 = Node(np.array([0.05, 0.9]), gra[3])

p5 = Node(np.array([0.01, 0.7]), gra[4])

prob = [p1, p2, p3, p4, p5]

bn = BN(gra, prob)

jp = []
ev = (-1, [], [], 1, 1)
print(bn.computePostProb(ev))
"""
for e1 in [0,1]:
    for e2 in [0, 1]:
        for e3 in [0, 1]:
            for e4 in [0, 1]:
                for e5 in [0, 1]:
                    jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))

print("sum joint %.3f (1)" % sum(jp))
"""


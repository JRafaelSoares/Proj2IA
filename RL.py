"""
Joao Rafael Soares n87675
Maria Catarina Duarte n87681
Grupo 36
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""

import numpy as np
import random

from tempfile import TemporaryFile
outfile = TemporaryFile()

class finiteMDP:

    def __init__(self, nS, nA, gamma, P=[], R=[], absorv=[]):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((self.nS,self.nA))
        self.P = P
        self.R = R
        self.absorv = absorv
        # completar se necessario
        
            
    def runPolicy(self, n, x0,  poltype = 'greedy', polpar=[]):
        #nao alterar
        traj = np.zeros((n,4))
        x = x0
        J = 0
        for ii in range(0,n):
            a = self.policy(x,poltype,polpar)
            r = self.R[x,a]
            y = np.nonzero(np.random.multinomial( 1, self.P[x,a,:]))[0][0]
            traj[ii,:] = np.array([x, a, y, r])
            J = J + r * self.gamma**ii
            if self.absorv[x]:
                y = x0
            x = y
        
        return J,traj


    def VI(self):
        #nao alterar
        nQ = np.zeros((self.nS,self.nA))
        while True:
            self.V = np.max(self.Q,axis=1) 
            
            for a in range(0,self.nA):
                nQ[:,a] = self.R[:,a] + self.gamma * np.dot(self.P[:,a,:],self.V)
            
            err = np.linalg.norm(self.Q-nQ)
            
            self.Q = np.copy(nQ)
            
            if err<1e-7:
                break
            
        #update policy
        self.V = np.max(self.Q,axis=1) 
        #correct for 2 equal actions
        self.Pol = np.argmax(self.Q, axis=1)
                    
        return self.Q,  self.Q2pol(self.Q)

            
    def traces2Q(self, trace):
        # implementar esta funcao
        self.Q = np.zeros((self.nS,self.nA))
        while True:
            oldQ = np.copy(self.Q)
            for trajectory in trace:
                initialState = int(trajectory[0])
                action = int(trajectory[1])
                finalState = int(trajectory[2])
                reward = int(trajectory[3])
                alpha = 0.2
                
                self.Q[initialState][action] = self.Q[initialState][action] + alpha*(reward + self.gamma*np.amax(self.Q[finalState]) - self.Q[initialState][action])
            error = np.linalg.norm(self.Q - oldQ)
            
            if error<1e-7:
                break
        return self.Q
    
    def policy(self, x, poltype = 'exploration', par = []):
        # implementar esta funcao
        
        if poltype == 'exploitation':
            a = np.argmax(par[x])

            
        elif poltype == 'exploration':
            #a = np.argmax(boltzman[x])
            a = np.random.randint(len(self.Q[x]), size = 1)[0]
        return a
    
    def Q2pol(self, Q, eta=5):
        # implementar esta funcao
        ones = np.ones((len(Q[0]), len(Q[0])))
        return np.exp(eta*Q)/np.dot(np.exp(eta*Q),ones)


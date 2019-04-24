#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:04:36 2018

@author: gabriel
"""

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.integrate import trapz
import matplotlib.pyplot as plt

# solve laplace equation 
# laplacien F(x) = rho(x)

def rho(x):
    return 2 * x

def solveFiniteDiff(L = 1, N = 100, conditions = [['dirichlet', 1], ['dirichlet', 1]]):
    # x \in [0, L]
    h = L / N
    mesh = np.linspace(0, L, N)
    
    # build matrix
    #    A f = b
    
    b =  h**2 * rho(mesh)
    Adata = []
    Arow = []
    Acol = []
    
    # border contitions
    # x = 0
    if conditions[0][0] == 'dirichlet':
        Adata.append(1), Arow.append(0), Acol.append(0)
        b[0] = conditions[0][1]
    elif conditions[0][0] == 'newmann':
        Adata.append(-1), Arow.append(0), Acol.append(0)
        Adata.append(1), Arow.append(0), Acol.append(1)        
        b[0] = h* conditions[0][1]
    elif conditions[0][0] == 'robin':
        Adata.append(conditions[0][1] * h - conditions[0][2]), Arow.append(0), Acol.append(0)
        Adata.append(conditions[0][1] * conditions[0][2]), Arow.append(0), Acol.append(1)        
        b[0] = h
        
     # x = L   
    if conditions[1][0] == 'dirichlet':
        Adata.append(1), Arow.append(N - 1), Acol.append(N - 1)
        b[N - 1] = conditions[1][1]    
    elif conditions[1][0] == 'newmann':
        Adata.append(-1), Arow.append(N - 1), Acol.append(N - 2)
        Adata.append(1), Arow.append(N - 1), Acol.append(N - 1)        
        b[N - 1] = h* conditions[1][1]    
    elif conditions[1][0] == 'robin':
        Adata.append(conditions[1][1] * h + conditions[1][2]), Arow.append(N - 1), Acol.append(N - 1)
        Adata.append(conditions[1][2]), Arow.append(N - 1), Acol.append(N - 2)        
        b[N - 1] = h        
        
       
    
    # domain assembly
    for col in range(1, N - 1):
        Adata.append(1), Arow.append(col), Acol.append(col - 1)
        Adata.append(-2), Arow.append(col),  Acol.append(col)
        Adata.append(1), Arow.append(col), Acol.append(col + 1)
    
    A = csc_matrix((Adata, (Arow, Acol)), shape = (N, N))
        
    # inverse matrix
    return mesh, spsolve(A, b)

if __name__ == '__main__':
    # plot a single graph
    x, f = solveFiniteDiff(conditions = [['dirichlet', 0], ['newmann', 1]])
    plt.figure(1)
    plt.plot(x, f)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Numerical Solution of Newmann equation')
    
    # plot error for multiple N
    N = np.logspace(1, 3).astype(int)
    errors = np.zeros((N.shape))
    
    for i in range(N.size):
        x, f = solveFiniteDiff(N = N[i], conditions = [['dirichlet', 0], ['newmann', 1]])
        errors[i] = trapz(np.abs(x**3 / 3 - f), dx = 1 / N[i])
    
    plt.figure(2)
    plt.loglog(N, errors)
    plt.xlabel("N")
    plt.ylabel("error L1")
    plt.title('error as a function of discretization')

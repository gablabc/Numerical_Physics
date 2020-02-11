#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

def rho(x):
    return 2 * x

def solveFiniteDiff(L = 1, N = 100, conditions = [['dirichlet', 1], ['dirichlet', 1]], func = rho):
    """
    This function solves the system
    d^2f(x)/dx^2 = rho(x) for all x in [0, L]
    
    __Inputs__
    - L      (length of the interval)
    - N      (number of points in the mesh)
    - conditions list
    - func   (function rho in the equation)

    __Outputs__
    - list of x in mesh
    - values of f(x)

    the conditions lists is structured as follow
    [['condition name', values] , ['condition name', values']] 

    where the condition name can be dirichlet newmann or robin
    """
    h = L / N
    mesh = np.linspace(0, L, N)
    
    b =  h**2 * rho(mesh)
    Adata = []
    Arow = []
    Acol = []
    
    # Border conditions
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
        Adata.append(conditions[1][1] * h + conditions[1][2]), \
                        Arow.append(N - 1), Acol.append(N - 1)
        Adata.append(conditions[1][2]), Arow.append(N - 1), Acol.append(N - 2)        
        b[N - 1] = h        
        
       
    
    # Domain assembly
    for col in range(1, N - 1):
        Adata.append(1), Arow.append(col), Acol.append(col - 1)
        Adata.append(-2), Arow.append(col),  Acol.append(col)
        Adata.append(1), Arow.append(col), Acol.append(col + 1)
    
    # Assemble A as a sparse matrix
    A = csc_matrix((Adata, (Arow, Acol)), shape = (N, N))
        
    # Solve the system
    return mesh, spsolve(A, b)
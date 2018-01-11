#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:44:21 2018

@author: Ohi Dibua
This file contains the class that calculates the nodes and weights necessary to calculate
the integral of a function of some input x, with some dimenson, dim, and accuracy, level.
These values are currently obtained from a pre-calculated file. It also calculates the 
integral.

The inputs of the obtainNodesandWeightsKPU function are:
    dim: Dimension of input domain being integrated
    level: Accuracy of sparse integral
    
    returns table of nodes and weights
The inputs of the integrate function are:
    weights: Weights corresponding to each node
    f: Function evaluated at each node
"""
from pathlib import Path
import numpy as np
import sys

class performIntegral():        
    def obtainNodesandWeightsKPU(self,dim,level):
        #Load nodes and weights from file that contains them for a certain dimension and accuracy
        integralPath="./integralNodesWeights/KPU_d"+str(dim)+"/KPU_d"+str(dim)+"_l"+str(level)+".asc";
        integralFile = Path(integralPath,delimeter=",");
        if not integralFile.is_file():
            sys.exit("File containing this combination of nodes and weights does not exixst") 
        else:    
            integralTable=np.loadtxt(integralPath,delimiter=',');
            shpTable=np.shape(integralTable);
        return (integralTable[0:,0:dim],integralTable[0:,-1])
    #Calculates integral  
    def integrate(self,weights,f):
        I = 0;    
        for j in range(len(f)):          
            I = I + f[j]*weights[j];
        return I
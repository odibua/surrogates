#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:35:57 2018

@author: Ohi Dibua
Test code for PCE. Shows that the code does a good job of constructing surrogates 
of functions.
"""
import sys
import numpy as np
from testFunctions import *
from generatePCE import genPCEIntegral
from generateLegendrePolynomials import customLegendre

testFuncArr = ['nDLinear','nDCubic']
#Inputs to code that prescribe function to be used in testing, max individual polynomial power,
#level of accuracy of integrals, and dimension of input to function
chooseTestFunc = sys.argv[1]; p = int(sys.argv[2]); level=int(sys.argv[3]); n = int(sys.argv[4]);

#Checks to make sure that inputs are valid
if (chooseTestFunc not in testFuncArr ):
    sys.exit('Not a valid test function. Select either nDLinear or nDCubic');
elif (n<1):
    sys.exit('Not a valid dimension of input. Choose integer >= 1');
elif (level<1):
    sys.exit('Not a valid level of accuracy. Must be >=1')
elif (p<(level-1)):
    sys.exit('Not a valid maximum polynomial power. Select p to be <= level')
#chooseTestFunc = testFuncArr[3];
#p = 3; #Maximum Polynomial Degree
#n = 5;
#level = 4; #Level of accuracy in sparse grid integration

if (chooseTestFunc == 'nDLinear'):
    funcUse = nDLinFunc
    d=n;
elif (chooseTestFunc == 'nDCubic'):
    funcUse = nDCubedFunc
    d=n;

#Perform PCE expanion and obtain coefficients, nodes and weights of integral, and list
#of polynomial powers. Does assumption based on legendre polynomials.   
beta,polynomial,nodes,weights,powList,integralArr = genPCEIntegral(p,d,level,customLegendre,funcUse);

#Uses expansion coefficeints to make approximation to real functions in domain
#and checks for the errors.
nTest=10;
x = np.zeros((nTest,d)); 
fAct=[]; fEst=[]; err=[];
lb=-1; ub=1;
for l in range(nTest):
    fTemp=0;
    x[l,0:] = (ub-lb)*np.random.random(d) + lb
    for k in range(len(beta)): 
        poly=1.0;
        for j in range(d):
            poly=poly*customLegendre(powList[k][j],np.array([x[l][j]]));
        fTemp = fTemp+beta[k]*poly
    fAct.append(funcUse(np.array(x[l,0:])));
    fEst.append([fTemp]);
    err.append(np.abs(fAct[l]-fEst[l])/fAct[l])
print('err',err)
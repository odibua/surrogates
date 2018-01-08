#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:35:57 2018

@author: odibua
"""

import numpy as np
from testFunctions import *
from generatePCE import genPCEIntegral
from generateLegendrePolynomials import customLegendre

testFuncArr = ['Linear','nDLinear','Cubic','nDCubic']
chooseTestFunc = testFuncArr[3];

p = 3; #Maximum Polynomial Degree
n = 5;
level = 4; #Level of accuracy in sparse grid integration

if chooseTestFunc == testFuncArr[0]:
    funcUse = linFunc; 
    d=1;
elif (chooseTestFunc == testFuncArr[1]):
    funcUse = nDLinFunc
    d=n;
elif (chooseTestFunc == testFuncArr[2]):
    funcUse = cubedFunc
    d=1;
elif (chooseTestFunc == testFuncArr[3]):
    funcUse = nDCubedFunc
    d=n;
    
beta,polynomial,nodes,weights,powList = genPCEIntegral(p,d,level,customLegendre,funcUse);

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
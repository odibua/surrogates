#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:10:51 2018

@author: odibua
"""

import numpy as np

def linFunc(x):
    return x+5

def nDLinFunc(x):
      return np.sum([x[k] for k in range(len(x))])+5

def cubedFunc(x):
    return x**3+5;

def nDCubedFunc(x):
    return sum([x[k]**3 for k in range(len(x))])+5;



    
    
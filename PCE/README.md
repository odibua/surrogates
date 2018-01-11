# Polynomial Chaos Expansion

This folder contains files used for constructing generalized polynomial chaos expansions(PCE) of functions according to [1].It is constructed
using integrals based on smolyak's cubature as illustrated in Section 2.3.4 which converges faster than Monte Carlo.

[1] T. Crestaux, O. Maitre, J-M Martinez, "Polynomial Chaoes expansion for sensitivity analysis," 
    Reliability Engineering and System Safety, 2008
    
# Running Tests 

The file testPCE tests the generalized polynomial chaos expansion. It is necessary for the user to input, in a terminal,
the following arguments.

    chooseTestFunc = sys.argv[1]; p = int(sys.argv[2]); level=int(sys.argv[3]); n = int(sys.argv[4]);

The allowed test functions are:

    testFuncArr = ['nDLinear','nDCubic']
    
and the code checks to insure that the values of p, the maximum power allowed in a single polynomial, level, which is the 
level of accuracy of a quadrature at a given dimension, and n, which is the dimension of the input function. The generalized PCE is constructed using:

    beta,polynomial,nodes,weights,powList = genPCEIntegral(p,d,level,customLegendre,funcUse);
    
and it returns beta, coefficient of expansion, polynomial, which is the associated orthogonal polynomial at some set of nodes, 
weights associated with each node, and powList, the list of powers in each dimension that is contained at each associated polynomial. Finally, the below block of code constructs an approximation of the function and returns the error.

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



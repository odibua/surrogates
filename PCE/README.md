# Polynomial Chaos Expansion

This folder contains files used for constructing generalized polynomial chaos expansions of functions according to [1].It is constructed
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
level of accuracy of a quadrature at a given dimension, and n, which is the dimension of the input function.



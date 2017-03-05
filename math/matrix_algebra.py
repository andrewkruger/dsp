# Matrix Algebra

import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

print "1. Matrix Deminsions (m x n)"
print "1.1) A:", A.shape
print "1.2) B:", B.shape
print "1.3) C:", C.shape
print "1.4) D:", D.shape
print "1.5) u:", u.shape
print "1.6) w:", w.shape

alpha = 6
print "\n2. Vector Operations"
print "2.1) u+v =", u+v
print "2.2) u-v =", u-v
print "2.3) alpha * u =", alpha*u
print "2.4) u dot v =", np.matmul(u,v)
print "2.5) |u| =", np.linalg.norm(u)

print "\n3. Matrix Operations"
print "3.1) A+C is not defined because the two matrices need the same shape, "\
    "but A has shape", A.shape, "and C has shape", C.shape
print "\n3.2) A-C^T ="
print A-C.T
print "\n3.3) C^T+3D ="
print C.T+3*D
print "\n3.4) B*A ="
print np.matmul(B,A)
print "\n3.5) B*A^T is not defined because the second dimension of B (which is ", B.shape[1],") needs to be" \
    " the same as the first dimension of A^T (which is ", A.T.shape[0], ")."
print "\n3.6) B*C is not defined because the second dimension of B (which is ", B.shape[1],") needs to be" \
    " the same as the first dimension of C (which is ", C.shape[0], ")."
print "\n3.7) C*B ="
print np.matmul(C,B)
print "\n3.8) B^4 ="
print np.linalg.matrix_power(B,4)
print "\n3.9) A*A^T ="
print np.matmul(A,A.T)
print "\n3.10) D^T*D ="
print np.matmul(D.T,D)

# Do not change these variables
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

# Q1: record the dimensions of A, B, C, D, u, v respectively in the dict below. 
#     Do not type the answers, make python do the work

dimensions = {
    'A': A.shape,
    'B': B.shape,
    'C': C.shape,
    'D': D.shape,
    'u': u.shape,
    'v': v.shape
}

# Q2: vector operations
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
alpha = 6

u_plus_v = u+v            # u+v
u_minus_v = u-v           # u-v
alpha_times_u = alpha*u       # alpha * u, alpha = 6
u_dot_v = np.dot(u,v)             # u . v
norm_u = np.linalg.norm(u)              # ||u|| 


# Q3: compute the following and assign to variables below:
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work

try:
    A_plus_C = A + C             # A + C
except:
    A_plus_C = None

A_minus_Ctranspose = A - np.transpose(C)   # A - C.T
Ctranspose_plus_3D = np.transpose(C) + 3*D   # C.T + 3*D
B_times_A = np.matmul(B, A)            # B*A

try:
    B_times_Atranspose = np.matmul(B,np.transpose(A))   # B*A.T
except:
    B_times_Atranspose = None

# Q4: (bonus)

try:
    B_times_C = np.matmul(B, C)            # B*C
except:
    B_times_C = None
    
C_times_B = np.matmul(C, B)            # C*B
B_exp_4 = np.linalg.matrix_power(B, 4)              # B^4
A_times_Atranspose = np.matmul(A,np.transpose(A))
Dtranspose_times_D = np.matmul(np.transpose(D), D)   # D.T*D


''' Original (pre-HackerRank)

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


==============OUTPUT================
1. Matrix Deminsions (m x n)
1.1) A: (2, 3)
1.2) B: (2, 2)
1.3) C: (3, 2)
1.4) D: (2, 3)
1.5) u: (4,)
1.6) w: (4, 1)

2. Vector Operations
2.1) u+v = [ 9  7 -4  9]
2.2) u-v = [ 3 -3 -2  1]
2.3) alpha * u = [ 36  12 -18  30]
2.4) u dot v = 51
2.5) |u| = 8.60232526704

3. Matrix Operations
3.1) A+C is not defined because the two matrices need the same shape, but A has shape (2, 3) and C has shape (3, 2)

3.2) A-C^T =
[[-4 -7 -3]
 [ 3  6  4]]

3.3) C^T+3D =
[[14  3  3]
 [ 2  7  9]]

3.4) B*A =
[[-1 -5 -1]
 [ 2  7  4]]

3.5) B*A^T is not defined because the second dimension of B (which is  2 ) needs to be the same as the first dimension of A^T (which is  3 ).

3.6) B*C is not defined because the second dimension of B (which is  2 ) needs to be the same as the first dimension of C (which is  3 ).

3.7) C*B =
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]

3.8) B^4 =
[[ 1 -4]
 [ 0  1]]

3.9) A*A^T =
[[14 28]
 [28 69]]

3.10) D^T*D =
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
 '''

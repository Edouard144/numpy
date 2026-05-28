import numpy as np

# =============================
# NUMPY LINEAR ALGEBRA BASICS
# =============================

# 1. VECTORS
print("VECTOR OPERATIONS")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a)
print("b:", b)

# Dot product
print("Dot product:", np.dot(a, b))

print("\n====================")

# 2. MATRICES
print("MATRIX OPERATIONS")
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("A:\n", A)
print("B:\n", B)

# Matrix multiplication
print("Matrix multiplication (np.matmul):")
print(np.matmul(A, B))

print("Matrix multiplication (@ operator):")
print(A @ B)

print("\n====================")

# 3. TRANSPOSE
print("TRANSPOSE")
C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("C:\n", C)
print("Transpose of C:\n", C.T)

print("\n====================")

# 4. IDENTITY MATRIX
print("IDENTITY MATRIX")
I = np.eye(3)
print(I)

print("\n====================")

# 5. PRACTICE SECTION
print("PRACTICE")
x = np.array([2, 3, 4])
y = np.array([1, 0, 2])

print("x:", x)
print("y:", y)
print("Dot product x·y:", np.dot(x, y))

M1 = np.array([
    [1, 2],
    [3, 4]
])

M2 = np.array([
    [2, 0],
    [1, 2]
])

print("M1 @ M2:\n", M1 @ M2)
print("Transpose of M1:\n", M1.T)
print("Identity matrix 4x4:\n", np.eye(4))
import numpy as np

# =============================
# NUMPY RANDOM BASICS
# =============================

# 1. Random number (0 to 1)
print("Random number (0-1):")
print(np.random.rand())

print("\n====================")

# 2. Random array (0 to 1)
print("Random array (5 values):")
a = np.random.rand(5)
print(a)

print("\n====================")

# 3. Random integer (single value)
print("Random integer (1 to 9):")
print(np.random.randint(1, 10))

print("\n====================")

# 4. Random integer array
print("Random integer array (5 values):")
b = np.random.randint(1, 10, 5)
print(b)

print("\n====================")

# 5. Random 2D array (matrix)
print("Random 3x3 matrix:")
c = np.random.randint(1, 100, (3, 3))
print(c)

print("\n====================")

# 6. Shuffle array
print("Shuffled array:")
d = np.array([1, 2, 3, 4, 5])
np.random.shuffle(d)
print(d)

print("\n====================")

# 7. Random choice
print("Random choice from array:")
e = np.array([10, 20, 30, 40])
print(np.random.choice(e))

print("\n====================")

# =============================
# MINI PRACTICE SECTION
# =============================

print("Mini Practice:")

arr = np.random.randint(1, 50, 10)
print("Original array:", arr)

np.random.shuffle(arr)
print("Shuffled array:", arr)

print("Random picked value:", np.random.choice(arr))

matrix = np.random.randint(1, 100, (2, 3))
print("2x3 matrix:")
print(matrix)